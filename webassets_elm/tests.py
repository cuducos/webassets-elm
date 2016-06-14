from unittest import TestCase
from webassets.filter import register_filter
from webassets.test import TempEnvironmentHelper
from webassets_elm import Elm


register_filter(Elm)


class ElmFilterTestCase(TempEnvironmentHelper, TestCase):

    elm_code = 'import Html exposing (h1, text)\nmain = h1 [] [text "I<3elm"]'
    default_files = {'main.elm': elm_code}

    def setUp(self):
        super(ElmFilterTestCase, self).setup()

    def test_elm_filter(self):
        self.mkbundle('main.elm', filters='elm', output='app.js').build()
        self.assertIn('I<3elm', self.get('app.js'))
