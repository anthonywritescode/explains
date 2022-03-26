# [don't run `python my/script.py`! (beginner - intermediate)](https://youtu.be/hgCVIa5qQhM)

Today I show why running `python my/script.py` is almost always not what you want and that `PYTHONPATH` isn't much better and that you usually want `python -m`!

## Interactive examples

### Bash

```bash
mkdir a
touch b.py a/main.py a/__init__.py

tree .

python a/main.py
python -m a.main

virtualenv venv
. venv/bin/activate
pip install .

a-main
ls venv/lib/python*/site-packages/

PYTHONPATH=. python a/main.py

touch a/b.py
PYTHONPATH=. python a/main.py
```
