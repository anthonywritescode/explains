# [how do from imports keep their globals? (intermediate)](https://www.youtube.com/watch?v=FSPyCD5P76A)

Today I show how imports work and how functions retain access to their global variables without needing to import them!

## Interactive examples

### Bash

```bash
babi t2.py
```

### Python

```python
from t2 import square
square()

import sys
sys.modules
sys.modules['t2']
sys.modules['t2'].num

dir(square)
square.__globals__
list(square.__globals__)
square.__globals__['num']

import dis
dis.dis(square)
square.__globals__['num'] = 9
square()

sys.modules['t2'].num
sys.modules['t2'].__dict__
list(sys.modules['t2'].__dict__)
```
