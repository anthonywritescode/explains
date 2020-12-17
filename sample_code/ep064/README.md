# [using the python \_\_import\_\_ builtin correctly (intermediate)](https://youtu.be/3V3bv7FsR48)

Today I talk about the `__import__` builtin in python and one example of how you might use it (as well as a tricky tip that you almost always want!)

## Interactive examples

### Python

```python
s = 'curses.COLOR_GREEN'
s = 'curses:COLOR_GREEN'
s2 = 'os.path:join'

s
modpart, _, attrpart = s.partition(':')
modpart
attrpart

import curses
import $modpart

__import__(modpart)
mod = __import__(modpart)
mod
getattr(mod, attrpart)
import curses
curses.COLOR_GREEN

modpart2, _, attrpart2 = s2.partition(':')
modpart2
attrpart2

__import__(modpart2)
__import__(modpart2).join
__import__(modpart2, fromlist=['_trash'])

import os.path
os.path

mod2 = __import__(modpart2, fromlist=['_trash'])
getattr(mod2, attrpart2)

__import__(modpart2)
import sys
sys.modules[modpart2]

from .foo import bar
```

### Bash

```bash
python3 -m pydoc __import__
python2 -m pydoc __import__
```
