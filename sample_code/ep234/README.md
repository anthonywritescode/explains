# [why doesn't flake8 mark this import as unused? (beginner - intermediate)](https://youtu.be/gRq3Sb0_dJM)

Today I talk about a quirk with `import`-imports and why flake8 doesn't mark one as "unused" (because it's actually potentially used!)

## Interactive examples

### Python

```python
dir()
always = set(dir())
always.add('always')

import a
set(dir()) - always

import a.b
set(dir()) - always

import sys
sys.modules['a.b']

import os
os.path
```

### Bash

```bash
flake8 t.py
mkdir a
touch a/__init__.py
touch a/b.py
echo 'x = 1' > a/__init__.py
python -m t
python -S
PYTHONSTARTUP= python

virtualenv venv
. venv/bin/activate
pip install reorder-python-imports

cp t.py t_old.py
reorder-python-imports t.py
cat t.py
mv t_old.py t.py

ls
touch a/x.py
echo '' > a/__init__.py
echo 'import a.x' > a/b.py
python -m t
```
