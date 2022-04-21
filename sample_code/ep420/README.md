# [I don't need `__init__.py`? PEP 420 and namespace packages (intermediate)](https://youtu.be/2Xvb79hOUdM)

Today I talk about namespace packages, what PEP 420 is, and why I don't use namespace packages

## Interactive examples

### Python

```python
import ns.a
import ns.b

import sys
sys.path


import ns.a
import ns.b
import ns

ns.a
ns.b
ns

ns.__loader__

import folder
folder

# Windows

import os
import Lib.os

Lib.os is os

import DLLs
import Doc
```

### Bash

```bash
mkdir root1 root2
mkdir root1/ns root2/ns

tree .

touch root1{1,2}/ns/_init__.py
touch root1/ns/a.py
touch root2/ns/b.py

tree .

PYTHONPATH=root1:root2 python

nano */*/__init__.py
PYTHONPATH=root1:root2 python

rm */*/__init__.py
find -name '*.pyc' -delete
tree .

PYTHONPATH=root1:root2 python
PYTHONPATH=root1:root2 python3.10

mkdir folder
folder
```

### Windows CMD

```batch
ls C:\Python310
ls C:\Python310\Lib
C:\Python310\python.exe
```
