from contextlib import contextmanager
from os import chdir, getcwd, remove
import os.path
from sys import platform
from tempfile import NamedTemporaryFile, TemporaryFile
from webassets.filter import ExternalTool

__all__ = ('Elm')


@contextmanager
def excursion(directory):
    """Context-manager that temporarily changes to a new working directory."""
    old_dir = getcwd()
    try:
        chdir(directory)
        yield
    finally:
        chdir(old_dir)


class Elm(ExternalTool):
    """Elm filter for webassets.

    Requires the ``elm-make`` to be available from the system path.

    Supports the following external configuration:

    ELM_MAKE_BIN
        The path to the ``elm-make`` binary. If not set, assumes ``elm-make``
        is in the system path.

    """

    name = 'elm'
    options = {'binary': 'ELM_MAKE_BIN',
               'change_directory': 'ELM_MAKE_CHANGE_DIRECTORY'}
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
        elm_make = self.binary or 'elm-make'
        change_directory = bool(self.change_directory or False)
        source = kw['source_path']
        source_dir = os.path.join(*os.path.split(source)[:-1])
        exec_dir = source_dir if change_directory else getcwd()
        write_args = [elm_make, source, '--output', tmp.name, '--yes']
        with excursion(exec_dir), \
             TemporaryFile(mode='w') as fake_write_obj:
            self.subprocess(write_args, fake_write_obj)

        # read the temp file
        cat_or_type = 'type' if platform == 'win32' else 'cat'
        read_args = [cat_or_type, tmp.name]
        self.subprocess(read_args, out)
        remove(tmp.name)
