# [python star imports (beginner - intermediate)](https://youtu.be/gJJVXB5JLUk)

Today I talk about star imports in python and why you shouldn't use them!

## Setup commands

```bash
virtualenv venv

. venv/bin/activate

pip install flake8 pyflakes
```

## Interactive examples

### Python

```python
dir()
from t import *
dir()

import t

before = set(dir())
from t import *
after = set(dir())
after - before

from pkg import *
dir()
```

### Bash

```bash
flake8 t.py
pyflakes t.py

flake8 t2.py

mkdir pkg
touch pkg/__init__.py
nano !$
```
