import os.path
import shutil
from io import StringIO
from tempfile import TemporaryDirectory

from webassets.filter import ExternalTool

__all__ = ["Elm"]


class Elm(ExternalTool):
    """Elm filter for webassets.

    Requires the ``elm-make`` to be available from the system path.

    Supports the following external configuration:

    ELM_BIN
        The path to the ``elm`` binary. If not set, assumes ``elm``
        is in the system path.

    ELM_OPTIMIZE (boolean)
        If set to True, turns on the Elm compiler optimizations.

    ELM_DEBUG (boolean)
        If set to True, turns on the Elm compiler time traveling debugger
        option.

    """

    name = "elm"
    options = {"binary": "ELM_BIN", "optimize": "ELM_OPTIMIZE", "debug": "ELM_DEBUG"}
    max_debug_level = None

    def input(self, _in, out, **kw):
        """
        Currently Elm does not write to stdout
        (https://github.com/elm-lang/elm-make/issues/177), so we need to
        write the compiled contents to a temporary file and then read it in
        order to output to stdout.
        """
        elm = self.binary or "elm"
        source = kw["source_path"]
        source_dir = os.path.dirname(source)
        args = [elm, "make", source]
        if self.optimize:
            args.append("--optimize")
        if self.debug:
            args.append("--debug")

        with TemporaryDirectory() as directory:
            compilation_result = os.path.join(directory, "output.js")
            args += ["--output", compilation_result]
            self.subprocess(args, StringIO(), cwd=source_dir)
            with open(compilation_result, "r") as compilation_result_file:
                shutil.copyfileobj(compilation_result_file, out)
