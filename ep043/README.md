# [introduction to tox (beginner - intermediate)](https://youtu.be/75WBE_qbpGk)

Today I explain the basics of using `tox` as an automation / testing tool!

## Setup commands

```bash
git clone git@github.com:asottile/pyupgrade
# OR
git clone https://github.com/asottile/pyupgrade

virtualenv venv
. venv/bin/activate
pip install tox
```

## Interactive examples

### Bash

```bash
cd pyupgrade
ls tox.ini
rm tox.ini
tox
tox --help | less
tox --skip-missing-interpreters
tox -e py38
tox -e py27
tox -e py38 -- tests -k fstring
tox --devenv venv
. venv/bin/activate
pip freeze -l
pytest tests
```
