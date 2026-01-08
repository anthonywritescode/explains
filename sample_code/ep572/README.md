# [adding test == others fail??? (intermediate)](https://youtu.be/BoZDpQnA-Xw)

today I show off a very strange bug in `black`'s testsuite -- and then how I found the problem which led to the fix!

## Setup commands

```bash
git clone git@github.com:psf/black
cd black/
```

## Interactive examples

### Python

```python
def test_nothing_1():
    pass
def test_nothing_2():
    pass
def test_nothing_3():
    pass
def test_nothing_4():
    pass
def test_nothing_5():
    pass
def test_nothing_6():
    pass
def test_nothing_7():
    pass
def test_nothing_8():
    pass
def test_nothing_9():
    pass
def test_nothing_10():
    pass
def test_nothing_11():
    pass
def test_nothing_12():
    pass
def test_nothing_13():
    pass
```

### Bash

```bash
git checkout 1abcffc
tox --devenv venv

nano tests/test_black.py

. venv/bin/activate
pip install -e .[d]
pytest tests -n 4

python -um pytest tests -v -n 4 | tee -a log
grep FAIL log
grep gw0 log
grep gw0 log | grep -Eo '(PASSED|FAILED).*$'
grep gw0 log | grep -Eo '(PASSED|FAILED).*$' | cut -d' ' -f2- > testlist
grep FAIL log
nano testlist

pip install detect-test-polution
detect-test-polution --help

detect-test-polution --testids-file testlist --failing-test $(tail -1 testlist)
pytest tests/test_black.py::TestFileCollection::test_get_sources_with_stdin_symlink_outside_root $(tail -1 testlist)
```
