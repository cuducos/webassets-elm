from sys import platform
from tempfile import mkstemp, TemporaryFile
from webassets.filter import ExternalTool

__all__ = ('Elm')


class Elm(ExternalTool):
    """Elm filter for webassets.

    Requires the ``elm-make`` to be available from the system path.

    Supports the following external configuration:

    ELM_MAKE_BIN
        The path to the ``elm-make`` binary. If not set, assumes ``elm-make``
        is in the system path.

    """

    name = 'elm'
    options = {'binary': 'ELM_MAKE_BIN'}
    max_debug_level = None

    def input(self, _in, out, **kw):
        """
        Currently Elm does not write to stdout
        (https://github.com/elm-lang/elm-make/issues/39), so we need to write
        the compiled contents to a temporary file and then read it in order to
        output to stdout.
        """

        # write to a temp file
        tmp = mkstemp(suffix='.js')
        bin = self.binary or 'elm-make'
        write_args = [bin, kw['source_path'], '--output', tmp[1], '--yes']
        with TemporaryFile(mode='w') as fake_write_obj:
            self.subprocess(write_args, fake_write_obj)

        # read the temp file
        cat_or_type = 'type' if platform == 'win32' else 'cat'
        read_args = [cat_or_type, tmp[1]]
        self.subprocess(read_args, out)
