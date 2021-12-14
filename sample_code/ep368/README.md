# [python: NewType vs aliases (intermediate)](https://youtu.be/9rRYeunzX8c)

Today is another python typing video -- NewType!  I talk about how you can utilize NewType and how it differs from aliases

## Interactive examples

### Python

```python
from typing import NewType
T = NewType("T", int)

T(1)
x = 1
T(x) is x
```

### Bash

```bash
virtualenv venv
. venv/bin/activate
pip install mypy

mypy t.py
```
