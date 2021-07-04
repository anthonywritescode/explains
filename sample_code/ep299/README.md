# [debugging mypy types (beginner - intermediate)](https://youtu.be/Pc6H3Pofhp8)

Today we're back talking about typing in mypy -- I show you two ways to debug types during type checking as well as a hint about the mysterious `*` that sometimes shows up!

## Interactive examples

### Bash

```bash
virtualenv venv
. venv/bin/activate
pip install mypy

mypy t.py
flake8 t.py

mypy t.py
echo $?
```
