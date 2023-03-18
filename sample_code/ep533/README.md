# [how I made pre-commit's github actions 3x faster (intermediate)](https://youtu.be/5K8k-bSDnU0)

Today I show how I reworked pre-commit's testsuite and github actions to greatly speed up the runs.  while the approach isn't universally applicable, some of the ideas may be helpful!

## Interactive examples

### Bash

```bash
. venv/bin/activate
pytest --help | less

ls tests/languages/
ls tests/languages/lua_test.py

coverage erase && coverage run -m pytest tests/languages/lua_test.py && coverage report --include pre_commit/languages/lua.py
```
