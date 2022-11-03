# [I don't use pytest-cov (intermediate)](https://youtu.be/sPgvHGkmd0U)

Today I talk through why I think pytest-cov is unnecessary and a little annoying.

## Interactive examples

### Bash

```bash
git clone git@github.com:asottile/astpretty
cd astpretty/

tox --devenv venv
. venv/bin/activate
pip install pytest-cov

pytest --cov=. --cov-fail-under=100 --cov-report=xml:coverage.xml tests

coverage erase
coverage run -m pytest tests
coverage report

pip install coverage-enable-subprocess
```
