import os
import os.path
import shutil
from io import StringIO
from tempfile import TemporaryDirectory

from webassets.filter import ExternalTool

__all__ = ('Elm')


class Elm(ExternalTool):
    """Elm filter for webassets.

    Requires the ``elm-make`` to be available from the system path.

    Supports the following external configuration:

    ELM_BIN (binary)
        The path to the ``elm`` binary. If not set, assumes ``elm``
        is in the system path.

    ELM_OPTIMIZE (boolean)
        If set, turn on the elm compiler optimizations.

    """

    name = 'elm'
    options = {'binary': 'ELM_BIN', 'optimize': 'ELM_OPTIMIZE'}
    max_debug_level = None

    def input(self, _in, out, **kw):
        """
        Currently Elm does not write to stdout
        (hthttps://github.com/elm-lang/elm-make/issues/177), so we need to
        write the compiled contents to a temporary file and then read it in
        order to output to stdout.
        """
        elm = self.binary or 'elm'
        source = kw['source_path']
        source_dir = os.path.dirname(source)
        args = [elm, 'make', source]
        if self.optimize or False:
            args.append('--optimize')

        with TemporaryDirectory("w+") as tempd:
            outf = os.path.join(tempd, "output.js")
            write_args = [*args, '--output', outf]
            self.subprocess(write_args, StringIO(), cwd=source_dir)
            with open(outf, "r") as inf:
                shutil.copyfileobj(inf, out)
