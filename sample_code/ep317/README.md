# [pytest: testing env variables (intermediate)](https://youtu.be/N15X_pQHckQ)

Today I talk about three strategies to test environment variables using pytest!

## Interactive examples

### Bash

```bash
python t.py
USER=someone-else python t.py

virtualenv venv
. venv/bin/activate

pip install pytest
pytest t.py

pip install tox
tox -e py39

pip install pytest-env
pytest t.py
tox -e py39
```
