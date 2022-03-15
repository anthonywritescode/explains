# [fix flaky tests with detect-test-pollution! (intermediate)](https://youtu.be/w5O4zTusyJ0)

Today I show off a brand new project we made on stream!  it automates detecting polluting tests

## Interactive examples

### Bash

Session 1:

```bash
# git clone https://github.com/pytest-dev/pytest
git clone git@github.com:pytest-dev/pytest
cd pytest/

tox -e py38-unittestextras-coverage --devenv venv
. venv/bin/activate

pip install detect-test-pollution
detect-test-pollution --tests ./testing/ --failing-test testing/test_helpconfig.py::test_version_verbose

nano $(git grep -l test_valid_setup_py)
```

Session 2:

```bash
cd pytest/
. venv/bin/activate

pytest --collect-only -q testing/test_doctest.py
pytest --collect-only -q testing/test_doctest.py > testids
nano !$

detect-test-pollution --help
detect-test-pollution --testids-file ./testids --failing-test testing/test_helpconfig.py::test_version_verbose

pip install setuptools --upgrade
detect-test-pollution --testids-file ./testids --failing-test testing/test_helpconfig.py::test_version_verbose
```
