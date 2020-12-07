# [python packaging: src layout (intermediate)](https://youtu.be/sW1qUZ_nSXk)

Today I explain the ./src/ layout for python packages and why you should probably use it (and why I don't bother)

## Setup commands

```bash
git clone git@github.com:asottile/pyupgrade
# git clone https://github.com/asottile/pyupgrade
cd pyupgrade

virtualenv tox_venv

. tox_venv/bin/activate

pip install tox
```

## Interactive examples

### Python

```python
import sys
sys.path

import pyupgrade
pyupgrade.__file__
```

### Bash

```bash
tox -e py37
tox -r -e py37

.tox/py37/bin/python setup.py sdist
virtualenv venv
. venv/bin/activate
pip install dist/pyupgrade-<version>.tar.gz
pyupgrade --help

pip install .
mkdir src
mv pyupgrade.py src/
tox -r -e py37

rm -rf dist/
.tox/py37/bin/python setup.py sdist
virtualenv venv
. venv/bin/activate
pip install dist/pyupgrade-<version>.tar.gz
pyupgrade --help
```
