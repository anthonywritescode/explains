# [debugging a broken cache!](https://youtu.be/bhUk7Vog108)

today I show a debugging technique that I used to make a bug report for a broken lru cache implementation!

## Setup commands

```bash
git clone git@github.com:asottile/pyupgrade
git clone git@github.com:getsentry/sentry-python
cd sentry-python/
```

## Interactive examples

### Python

```python
from _lru_cache import LRUCache

c1 = LRUCache(2)
c1.set('hello hello', True)
c1.get('hello hello')

c2 = c1.__copy__()
c2.set('hello hello', False)
c2.get('hello hello')

c1.get('hello hello')
```

### Bash

```bash
git rev-parse HEAD
git log origin/master -- sentry_sdk/_lru_cache.py

cd ..
cp sentry-python/sentry_sdk/_lru_cache.py .

cd pyupgrade/
virtualenv venv
./venv/bin/pip install pytest tokenize-rt

./venv/bin/pytest tests
TEST_GROUP=7 TOTAL_TEST_GROUPS=11 ./venv/bin/pytest tests --collect-only
TEST_GROUP=7 TOTAL_TEST_GROUPS=11 ./venv/bin/pytest tests --collect-only -q
TEST_GROUP=7 TOTAL_TEST_GROUPS=11 ./venv/bin/pytest tests --collect-only -q > testlists

head -100 testlists > testlist2
wc -l testlist2

. venv/bin/activate
xargs -d'\n' pytest < testlist2
xargs -d'\n' pytest -s < testlist2

head -5 <log_filename>
wc -l <log_filename>

python3 -m t
```
