# [finding and fixing test pollution! (intermediate)](https://youtu.be/FRteianaPMo)

Today I explain the concept of "test pollution" and then show a manual procedure for finding the polluting tests

## Interactive examples

### Bash

```bash
# git clone https://github.com/pytest-dev/pytest
git clone git@github.com:pytest-dev/pytest
cd pytest/

git rev-parse HEAD
tox --devenv venv
. venv/bin/activate

pytest t.py
pytest t.py::test_k2 t.py::test_k

# creation of testids file
xargs -d'\n' pytest < testids

split -n l/2 testids step1_
ls step1_a*

tail -1 step1_ab
tail -1 step1_ab >> step1_aa

xargs -d'\n' pytest < step1_aa
xargs -d'\n' pytest < step1_ab

rm test_aa

split -n l/2 step1_aa step2_
ls step2_a*

tail -1 step2_ab >> step2_aa
tail -1 step2_aa
tail -1 step2_ab

xargs -d'\n' pytest < step2_aa
xargs -d'\n' pytest < step2_ab
```
