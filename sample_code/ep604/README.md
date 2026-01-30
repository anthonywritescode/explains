# [coverage doesn't work on a mypy plugin?](https://youtu.be/PlpwPfCfLus)

well not by default!  I walk through how I figured out what was going on and ultimately found a solution to running coverage on a mypy plugin!  also some insight into how this same problem can happen elsewhere :)

## Interactive examples

### Bash

```bash
git@github.com:python/mypy.git
git clone git@github.com:asottile/typing-derive
cd typing-derive/

tox --devenv venv
. venv/bin/activate

coverage run -m pytest tests && coverage report
coverage run -m pytest tests && coverage combine && coverage report
coverage erase && coverage run -m pytest tests && coverage combine && coverage report

ls tests
ls tests-typing

nano tests-typing/typeddict_from_func/forward.py

nano typing_derive/impl.py
python -m mypy tests-typing/typeddict_from_func/forward.py
git checkout -- typing_derive

coverage erase && coverage run -m pytest tests && coverage run -m mypy tests-typing && coverage combine && coverage report
nano typing_derive/impl.py
coverage erase && coverage run -m pytest tests && coverage run -m mypy --show-traceback tests-typing && coverage combine && coverage report
git checkout -- typing_derive

cd ../mypy/
git grep 'os._exit'
git grep hard_exit
mypy --help | grep fast-exit
git grep fast-exit

cd -
coverage erase && coverage run -m pytest tests && coverage run -m mypy --no-incremental --no-fast-exit --show-traceback tests-typing && coverage combine && coverage report
```
