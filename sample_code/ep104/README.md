# [fixing NameError / TypeError in python type annotations (intermediate)](https://youtu.be/zH_F2xC0LOk)

Today I talk about a common pitfall in typing and how to fix it with forward annotations!  I also discuss `__future__` annotations and a silly project I created to backport the `__future__` flag!

## Interactive examples

### Bash

```bash
python t.py

virtualenv venv
. venv/bin/activate
pip install mypy

mypy t.py

deactivate
rm -rf venv/
virtualenv venv -ppython3.6
. venv/bin/activate

pip install future-annotations
python3.6 t.py
future-annotations-show t.py
```
