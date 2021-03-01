# [typing: Protocol + @runtime\_checkable (intermediate)](https://youtu.be/4y94mvp_rYw)

Today I follow up to the video about Protocol and show @runtime_checkable for doing some light structural type checking at runtime!

## Interactive examples

### Python

```python
C.__index__.__annotations__
Indexable.__index__.__annotations__

import collections.abc
collections.abc.
```

### Bash

```bash
virtualenv venv
. venv/bin/activate
pip install mypy

mypy t.py
python t.py
python -i t.py
```
