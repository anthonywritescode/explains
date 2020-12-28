# [tox --devenv (beginner - intermediate)](https://youtu.be/flJi2N3dDk0)

Today I talk a little bit more about `tox --devenv` -- a little feature that's changed how I build python virtualenvs!

## Setup commands

```bash
virtualenv venv
. venv/bin/activate
pip install tox
```

## Interactive examples

### Bash

```bash
git clone git@github.com:asottile/pyupgrade
# git clone https://github.com/asottile/pyupgrade

cd pyupgrade
# virtualenv venv && . venv/bin/activate && pip install -r requirements.txt && pip install -e . && pip install requirements-dev.txt
nano tox.ini
nano setup.py
nano setup.cfg

tox --devenv venv
. venv/bin/activate
pytest tests
pip freeze
grep deps tox.ini

tox -e py39 --devenv venv39
. venv39/bin/activate
python --version

tox -e pre-commit --devenv venvpc
. venvpc/bin/activate
pip freeze -l

deactivate
git clean -fxfd

rm tox.ini
git grep tox
tox --devenv venv
. venv/bin/activate
pytest tests
pip install pytest
```
