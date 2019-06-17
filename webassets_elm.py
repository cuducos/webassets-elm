from io import StringIO
from pathlib import Path
from tempfile import TemporaryDirectory

from webassets.filter import ExternalTool

__all__ = ("Elm",)


class Elm(ExternalTool):
    """Elm filter for webassets.

    Requires the ``elm-make`` to be available from the system path.

    Supports the following external configuration:

    ELM_BIN (string, path to Elm binary)
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
        """Currently Elm does not write to stdout
        (https://github.com/elm-lang/elm-make/issues/177), so we need to
        write the compiled contents to a temporary file and then read it in
        order to output to stdout."""
        elm = self.binary or "elm"
        source = Path(kw["source_path"])

        assert source.exists()
        assert source.is_file()

        command = [elm, "make", str(source)]
        if self.optimize:
            command.append("--optimize")
        if self.debug:
            command.append("--debug")

        with TemporaryDirectory() as directory, StringIO() as buffer_:
            compiled = Path(directory) / "output.js"
            command.extend(["--output", str(compiled)])
            self.subprocess(command, buffer_, cwd=str(source.parent))
            print(compiled.read_text(), file=out)
