from os import remove
from sys import platform
from tempfile import NamedTemporaryFile, TemporaryFile
from webassets.filter import ExternalTool

__all__ = ('Elm')


class Elm(ExternalTool):
    """Elm filter for webassets.

    Requires the ``elm-make`` to be available from the system path.

    Supports the following external configuration:

    ELM_MAKE_BIN
        The path to the ``elm-make`` binary. If not set, assumes ``elm-make``
        is in the system path.

    ELM_PACKAGE_BIN
        The path to the ``elm-package`` binary. If not set, assumes
        ``elm-package`` is in the system path.

    """

    name = 'elm'
    options = {
        'elm_make_binary': 'ELM_MAKE_BIN',
        'elm_package_binary': 'ELM_PACKAGE_BIN',
    }
    max_debug_level = None

    def input(self, _in, out, **kw):
        """
        Currently Elm does not write to stdout
        (https://github.com/elm-lang/elm-make/issues/39), so we need to write
        the compiled contents to a temporary file and then read it in order to
        output to stdout.
        """

        # first install/update elm-package dependencies
        elm_package = self.elm_package_binary or 'elm-package'
        install_args = [elm_package, 'install', '--yes']
        # set utf-8 to handle unicode bullet point symbols
        with TemporaryFile(mode='w', encoding='utf-8') as fake_write_obj:
            self.subprocess(install_args, fake_write_obj)

        # create a temp file
        tmp = NamedTemporaryFile(suffix='.js', delete=False)
        tmp.close()  # close it so windows can read it

        # write to a temp file
        elm_make = self.elm_make_binary or 'elm-make'
        source = kw['source_path']
        write_args = [elm_make, source, '--output', tmp.name, '--yes']
        with TemporaryFile(mode='w') as fake_write_obj:
            self.subprocess(write_args, fake_write_obj)

        # read the temp file
        cat_or_type = 'type' if platform == 'win32' else 'cat'
        read_args = [cat_or_type, tmp.name]
        self.subprocess(read_args, out)
        remove(tmp.name)
