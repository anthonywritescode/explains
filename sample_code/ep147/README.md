# [mypy's "implicit optional" (and why I disable it) (intermediate)](https://youtu.be/sc1JfhSvSII)

Today we talk about mypy's "implicit optional" and why I think it's better to not use it!

## Interactive examples

### Bash

```bash
virtualenv venv
. venv/bin/activate
pip install mypy

mypy t.py
python -m this
mypy t.py --no-implicit-optional
```
