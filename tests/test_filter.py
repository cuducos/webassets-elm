from pathlib import Path
from unittest import TestCase

from webassets.filter import register_filter
from webassets.test import TempEnvironmentHelper

from webassets_elm import Elm

MAIN = Path(__file__).parent / "Main.elm"
JSON = Path(__file__).parent / "elm.json"

register_filter(Elm)


class ElmFilterTestCase(TempEnvironmentHelper, TestCase):
    default_files = {"Main.elm": MAIN.read_text(), "elm.json": JSON.read_text()}

    def setUp(self):
        super(ElmFilterTestCase, self).setup()

    def test_elm_filter(self):
        self.mkbundle("Main.elm", filters="elm", output="app.js").build()
        self.assertIn("I ❤️ Elm", self.get("app.js"))
        self.assertIn("Compiled in DEV mode", self.get("app.js"))
        self.assertNotIn("Compiled in DEBUG mode", self.get("app.js"))

    def test_elm_filter_optimized(self):
        self.env.config["ELM_OPTIMIZE"] = True
        self.mkbundle("Main.elm", filters="elm", output="app.js").build()
        self.assertNotIn("Compiled in DEV mode", self.get("app.js"))
        self.assertNotIn("Compiled in DEBUG mode", self.get("app.js"))

    def test_elm_filter_debug(self):
        self.env.config["ELM_DEBUG"] = True
        self.mkbundle("Main.elm", filters="elm", output="app.js").build()
        self.assertNotIn("Compiled in DEV mode", self.get("app.js"))
        self.assertIn("Compiled in DEBUG mode", self.get("app.js"))
