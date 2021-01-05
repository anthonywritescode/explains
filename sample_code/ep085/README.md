# [sort your imports! (beginner - intermediate)](https://youtu.be/Sjor8PZXnaw)

Today I talk about how and why I sort my imports in python and the tooling I use to do it!

## Setup commands

```bash
git clone git@github.com:pre-commit/pre-commit
# git clone https://github.com/pre-commit/pre-commit
cd pre-commit
```

## Interactive examples

### Python

```python
from typing import Any, Dict, Optional, Sequence  # noqa: F401
from typing import Any
from typing import Dict  # noqa: F401
from typing import Optional
from typing import Sequence
```

### Bash

```bash
git blame -w pre_commit/clientlib.py
# git blame -w <filaname>
```
