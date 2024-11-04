.. image:: https://img.shields.io/github/actions/workflow/status/cuducos/webassets-elm/tests.yml?style=flat
  :target: https://github.com/cuducos/webassets-elm/actions/workflows/tests.yml
  :alt: Travis CI

.. image:: https://img.shields.io/pypi/status/webassets-elm.svg?style=flat
  :target: https://pypi.python.org/pypi/webassets-elm
  :alt: Status

.. image:: https://img.shields.io/pypi/v/webassets-elm.svg?style=flat
  :target: https://pypi.python.org/pypi/webassets-elm
  :alt: Latest release

.. image:: https://img.shields.io/pypi/pyversions/webassets-elm.svg?style=flat
  :target: https://pypi.python.org/pypi/webassets-elm
  :alt: Python versions

.. image:: https://img.shields.io/pypi/l/webassets-elm.svg?style=flat
  :target: https://pypi.python.org/pypi/webassets-elm
  :alt: License

Elm filter for webassets
########################

Filter for compiling `Elm <http://elm-lang.org>`_ files using `webassets <http://webassets.readthedocs.org>`_.

Install
*******

::

    pip install webassets-elm


Elm versions
============

As of version 0.2.0, this plugin requires **Elm 0.19** or newer (building with ``elm make``).

If you need to build your Elm project with ``elm-make`` (Elm 0.18 and older), you can pin your ``webassets-elm`` package to version ``0.1.7``.

Basic usage
***********

.. code:: python

    from webassets.filter import register_filter
    from webassets_elm import Elm

    register_filter(Elm)

Settings
========

**Optionally** as an evironment variable you can have:

* ``ELM_BIN``: alternative path to ``elm`` if it is **not** available globally (e.g. ``node_modules/.bin/elm``).

* ``ELM_OPTIMIZE``: enable the Elm compiler optimization option. Recommended for production output.

* ``ELM_DEBUG``: enable the Elm compiler debug option.

Examples
========

Flask with `flask-assets <http://flask-assets.readthedocs.io/>`_
----------------------------------------------------------------

.. code:: python

    from flask import Flask
    from flask_assets import Bundle, Environment
    from webassets.filter import register_filter
    from webassets_elm import Elm

    app = Flask(__name__)

    register_filter(Elm)
    assets = Environment(app)

    elm_js = Bundle('elm/main.elm', filters=('elm',), output='app.js')
    assets.register('elm_js', elm_js)

Django with `django-assets <http://django-assets.readthedocs.org>`_
-------------------------------------------------------------------

.. code:: python

    from django_assets import Bundle, register
    from webassets.filter import register_filter
    from webassets_elm import Elm

    register_filter(Elm)

    elm_js = Bundle('elm/main.elm', filters=('elm',), output='app.js')
    register('elm_js', elm_js)

Contributing
============

Feel free to `report an issue <http://github.com/cuducos/webassets-elm/issues>`_, `open a pull request <http://github.com/cuducos/webassets-elm/pulls>`_, or `drop <http://tech.lgbt/@cuducos>`_ a `line <https://bsky.app/profile/cuducos.me>`_.

Don't forget to write and run tests, and format code:

::

    uv run pytest

Please note you need ``elm`` binary available to run tests, here you can find different ways to `install Elm <http://elm-lang.org/install>`_.
