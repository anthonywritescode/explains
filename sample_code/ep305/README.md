# [python: why reload() is a bad idea (beginner - intermediate)](https://youtu.be/oOs2JQu8KEw)

Today I talk about `reload()` (which used to be a builtin -- now in `importlib`) and how it works and why you generally shouldn't use it.

## Interactive examples

### Python

```python
from t import PLACEHOLDER
from t import C
import t

t.hello_hello()
import t
t.hello_hello()

import sys
sys.modules['t']

PLACEHOLDER is t.PLACEHOLDER
C is t.C

# edit the t.py file

import importlib
importlib.reload(t)
t.hello_hello()

PLACEHOLDER is t.PLACEHOLDER
C is t.C
C == t.C
```
