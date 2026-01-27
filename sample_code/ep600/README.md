# [3 way test pollution!](https://youtu.be/qbLhVVRSb14)

today I talk about a class of test pollution where three tests have to interact in a particular order to break a test!

## Setup commands

```bash
git clone git@github.com:getsentry/sentry
cd sentry/
```

## Interactive examples

### Python

```python
import signal
signal.alarm(1)
```

### Bash

```bash
git checkout <commit_hash>
git apply patch.discovery
git diff

nano testlist
grep -n 'tests/sentry/templatetags/test_sentry_helpers.py::test_org_url' testlist
head -n 1120 testlist > testlist2

detect-test-pollution --testids-file testlist2 --failing-test "$(tail -1 testlist2)"

wc -l 3way-1
python3 runt.py 3way-1

nano 3way-1
python3 runt.py 3way-1
python3

git branch
git branch <branch_name>
git show <branch_name> | git apply
python3 runt.py 3way-1 -vv

cat 3way-2
python3 runt.py 3way-2

nano src/sentry/app.py
nano src/sentry/middleware/env.py

git branch
git show <branch_name>

babi 3way-3
python3 runt.py !$ -vv
git show <branch_name>
```
