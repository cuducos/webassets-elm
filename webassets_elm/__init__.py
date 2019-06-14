import os
import os.path
from sys import platform
from tempfile import NamedTemporaryFile, TemporaryFile

from webassets.filter import ExternalTool

__all__ = ('Elm')


class Elm(ExternalTool):
    """Elm filter for webassets.

    Requires the ``elm-make`` to be available from the system path.

    Supports the following external configuration:

    ELM_BIN
        The path to the ``elm`` binary. If not set, assumes ``elm``
        is in the system path.

    """

    name = 'elm'
    options = {'binary': 'ELM_BIN'}
    max_debug_level = None

    def input(self, _in, out, **kw):
        """
        Currently Elm does not write to stdout
        (https://github.com/elm-lang/elm-make/issues/39), so we need to write
        the compiled contents to a temporary file and then read it in order to
        output to stdout.
        """
        # create a temp file
        tmp = NamedTemporaryFile(suffix='.js', delete=False)
        tmp.close()  # close it so windows can read it

        # write to a temp file
        elm = self.binary or 'elm'
        source = kw['source_path']
        source_dir = os.path.dirname(source)
        write_args = [elm, 'make', source, '--output', tmp.name]
        with TemporaryFile(mode='w') as fake_write_obj:
            self.subprocess(write_args, fake_write_obj, cwd=source_dir)

        # read the temp file
        cat_or_type = 'type' if platform == 'win32' else 'cat'
        read_args = [cat_or_type, tmp.name]
        self.subprocess(read_args, out)
        os.remove(tmp.name)
