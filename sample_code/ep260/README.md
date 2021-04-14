# [pytest: xfail vs xpass and all test statuses (beginner - intermediate)](https://youtu.be/uzodcMcHbJU)

Today I talk about all the different types of statuses that a pytest test can have!  I also explain my rationale for using xfail vs skip

## Interactive examples

### Bash

```bash
virtualenv venv
. venv/bin/activate
pip install pytest

pytest t.py
pytest -v t.py
echo $?
```
