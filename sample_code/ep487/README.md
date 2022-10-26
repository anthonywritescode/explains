# [pytest: everything you need to know about fixtures (intermediate)](https://youtu.be/ScEQRKwUePI)

Today I go over all the options and use cases for fixtures in pytest!

## Interactive examples

### Bash

```bash
virtualenv venv
. venv/bin/activate

pip install pytest

pytest t.py
pytest !$

pytest -s t.py
pytest -s t.py -k test_with_setup_teardown
pytest -s t.py -k test_g

pytest -s t.py -k test_with_setup_teardown
pytest -s t.py

pytest -s t.py -k My
```
