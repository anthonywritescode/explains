# [some weird django test database quirks](https://youtu.be/cyZ2fWVdxwE)

today I show two surprises I found when debugging work tests and django!

## Setup commands

```bash
git clone git@github.com:getsentry/sentry
cd sentry/
```

## Interactive examples

### Bash

```bash
babi tests/wat.py
pytest !$

pytest tests/wat.py
pytest tests/wat.py -v

nano t
pip install detect-test-pollution
pytest -p detect_test_pollution --dtp-testids-input-file t tests/wat.py
```
