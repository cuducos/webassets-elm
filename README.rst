Elm filter for webassets
########################

.. image:: https://img.shields.io/travis/cuducos/webassets-elm.svg?style=flat
  :target: https://travis-ci.org/cuducos/webassets-elm
  :alt: Travis CI

.. image:: https://img.shields.io/coveralls/cuducos/webassets-elm.svg?style=flat
  :target: https://coveralls.io/github/cuducos/webassets-elm
  :alt: Covearge

.. image:: https://landscape.io/github/cuducos/webassets-elm/master/landscape.svg?style=flat
  :target: https://landscape.io/github/cuducos/webassets-elm/master
  :alt: Code Health

Filter for compiling `Elm <http://elm-lang.org>`_ files using `webassets <http://webassets.readthedocs.org>`_.

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

Install
*******

::

    pip install webassets-elm

Basic usage
***********

.. code:: python

    from webassets.filter import register_filter
    from webassets_elm import Elm

    register_filter(Elm)

Settings
========

**Optionally** as an evironment variable you can have:

* ``ELM_BIN``: alternative path to ``elm`` if it is **not** available globally (e.g. ``node_modules/.bin/elm``)

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

Feel free to `report an issue <http://github.com/cuducos/webassets-elm/issues>`_, `open a pull request <http://github.com/cuducos/webassets-elm/pulls>`_, or `drop a line <http://twitter.com/cuducos>`_.

Don't forget to write and run tests:

::

    python setup.py test

You need ``elm`` binaries available to run tests. `Install Elm <http://elm-lang.org/install>`_ and then the required packages:

::

    elm-package install