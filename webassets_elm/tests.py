from unittest import TestCase
from webassets.filter import register_filter
from webassets.test import TempEnvironmentHelper
from webassets_elm import Elm


register_filter(Elm)


ELMJSON = """
{
    "type": "package",
    "name": "webassets-elm/test",
    "summary": "this is only here because we want to be able to run tests",
    "license": "BSD-3-Clause",
    "version": "1.0.0",
    "exposed-modules": [],
    "elm-version": "0.19.0 <= v < 0.20.0",
    "dependencies": {
        "elm/core": "1.0.0 <= v < 2.0.0",
        "elm/html": "1.0.0 <= v < 2.0.0"
    },
    "test-dependencies": {}
}
"""


class ElmFilterTestCase(TempEnvironmentHelper, TestCase):

    elm_code = 'import Html exposing (h1, text)\nmain = h1 [] [text "I<3elm"]'
    default_files = {'main.elm': elm_code, 'elm.json': ELMJSON}

    def setUp(self):
        super(ElmFilterTestCase, self).setup()

    def test_elm_filter(self):
        self.mkbundle('main.elm', filters='elm', output='app.js').build()
        self.assertIn('I<3elm', self.get('app.js'))

    def test_elm_filter_optimized(self):
        self.env.config['ELM_OPTIMIZE'] = True
        self.mkbundle('main.elm', filters='elm', output='app.js').build()
        self.assertNotIn('Compiled in DEV mode', self.get('app.js'))
