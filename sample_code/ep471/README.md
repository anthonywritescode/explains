# [how do from imports keep their globals? (intermediate)](https://youtu.be/FSPyCD5P76A)

Today I show how imports work and how functions retain access to their global variables without needing to import them!

## Interactive examples

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

### Bash

```bash
python
```
