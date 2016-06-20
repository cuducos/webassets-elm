# Elm filter for webassets

[![Status: Beta](https://img.shields.io/pypi/status/webassets-elm.svg)](https://pypi.python.org/pypi/webassets-elm)
[![Latest release](https://img.shields.io/pypi/v/webassets-elm.svg?style=flat)](https://pypi.python.org/pypi/webassets-elm)
[![Python Version](https://img.shields.io/pypi/pyversions/webassets-elm.svg?style=flat)](https://pypi.python.org/pypi/webassets-elm) 
[![Downloads](https://img.shields.io/pypi/dm/webassets-elm.svg?style=flat)](https://pypi.python.org/pypi/webassets-elm)
[![License](https://img.shields.io/pypi/l/webassets-elm.svg?style=flat)](https://pypi.python.org/pypi/webassets-elm)

[![Travis CI](https://img.shields.io/travis/cuducos/webassets-elm.svg?style=flat)](https://travis-ci.org/cuducos/webassets-elm)
[![Covearge](https://img.shields.io/coveralls/cuducos/webassets-elm.svg?style=flat)](https://coveralls.io/github/cuducos/webassets-elm)
[![Code Health](https://landscape.io/github/cuducos/webassets-elm/master/landscape.svg?style=flat)](https://landscape.io/github/cuducos/webassets-elm/master)

Filter for compiling [Elm](http://elm-lang.org) files using [webassets](http://webassets.readthedocs.org).

## Requirements

The `elm-make` binary has to be available from your system path. If it is not available you can:

* Configure an alternative path to `elm-make` with the `ELM_MAKE_BIN` variable (e.g. `node_modules/.bin/elm-make`)
* Install it globally using `$ npm i -g elm` or with [any of these methods](http://elm-lang.org/install)

## Install

```console
python -m pip webassets-elm
```

## Basic usage

```python
from webassets.filter import register_filter
from webassets_elm import Elm

register_filter(Elm)
```

### Flask example

Using [flask-assets](http://flask-assets.readthedocs.io/):

```python
from flask import Flask
from flask_assets import Bundle, Environment
from webassets.filter import register_filter
from webassets_elm import Elm

app = Flask(__name__)

register_filter(Elm)
assets = Environment(app)

elm_js = Bundle('elm/main.elm',
                filters=('elm',),
                output='app.js',
                depends='**/*.elm')
assets.register('elm_js', elm_js)

```

### Django example 

Using [django-assets](http://django-assets.readthedocs.org):

```python
from django_assets import Bundle, register
from webassets.filter import register_filter
from webassets_elm import Elm

register_filter(Elm)

elm_js = Bundle('elm/main.elm',
                filters=('elm',),
                output='app.js',
                depends='**/*.elm')
register('elm_js', elm_js)
```

## Contributing

Feel free to [report an issue](http://github.com/cuducos/webassets-elm/issues), [open a pull request](http://github.com/cuducos/webassets-elm/pulls), or [drop a line](http://twitter.com/cuducos).

Don't forget to write and run tests:

```console
python setup.py test
```

You need `elm` binaries available to run the tests. [Install Elm](http://elm-lang.org/install) and then the required packeges packages:

```console
elm-package install
```


## License

Copyright (c) 2016 Eduardo Cuducos

Licensed under the [MIT License](LICENSE).
