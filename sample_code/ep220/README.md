# [finding python source code and docs (beginner)](https://youtu.be/DUG77pRVsV8)

Today I show a few tricks to finding the source code for a module in python!

## Interactive examples

### Python

```python
import argparse
argparse

import _collections
_collections
```

### Bash

```bash
python -m pydoc argparse
python -m pydoc _collections
python -m pydoc sqlite3
python2 -m pydoc argparse
```
