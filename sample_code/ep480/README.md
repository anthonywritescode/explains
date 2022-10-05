# [what is coverage? (intermediate)](https://youtu.be/eQM3TOjsM_Q)

Today I talk about `coverage` -- a useful tool to help you figure out whether your code is actually tested!

## Interactive examples

### Python

```python
import sys
sys.settrace(lambda *a, **k: print(a, k))

print('hi')
x = 1

breakpoint()
print(1)
```

### Bash

```bash
virtualenv venv
. venv/bin/activate
pip install coverage pytest

coverage --help
coverage run -m pytest t.py

ls .coverage
sqlite3 .coverage
# .schema

coverage report
coverage report --show-missing

coverage run --branch -m pytest t.py
coverage report --show-missing

coverage html
firefox htmlcov/ &

coverage report --show-missing --fail-under 100
echo $?
```
