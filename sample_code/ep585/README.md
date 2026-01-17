# [how does python's module `__getattr__` actually work?](https://youtu.be/K1-wYUSQoF8)

today I walk you through a bit of a deep dive into how modules work, what we used to do before this feature, and where the magic lives in cpython!

## Setup commands

```bash
git@github.com:python/cpython
```

## Interactive examples

### Python

```python
import t
t.foo

import sys
sys.modules
sorted(sys.modules)

class C:
    def __getattr__(self, x):
        print(f'looking up {x}')
        return x * 2

sys.modules['c'] = C()
import c
c
c.foo

src = open('/usr/lib/python3.13/typing.py').read()
globs = {'__name__': 'typing'}
exec(src, globs)

typing = type('typing', (), globs)
typing

typing.OrderedDict
typing.Match

typing.__getattr__
typing().Match

import sys
import os
os
import typing
typing
type(typing)

import types
types.ModuleType

type(os)
import sys
type(sys)

import _decimal
type(_decimal)
```

### Bash

```bash
python3

git clone git@github.com:asottile/flake8-typing-imports
cd flake8-typing-imports/

nano flake8_typing_imports.py
nano bin/build-generated

git log -- bin/build-generated
git checkout <commit_hash>
nano bin/build-generated

python 3.13 -m pydoc typing
nano /usr/lib/python3.13/typing.py

python3.13

cd ../cpython/
ls Python/
ls Objects/
ls Modules/

nano Objects/moduleobject.c

cd ../flake8-typing-imports/
git checkout main
nano bin/build-generated
```
