# [NEW generic / alias syntax for python 3.12 (PEP 695) (intermediate)](https://youtu.be/YaDYUQ5mD5Q)

Today we go over the new syntax added in python 3.12 for generics and type aliases!

## Interactive examples

### Python

```python
type NumberTypes = int | float

OldNumberTypes = int | float

isinstance(1, OldNumberTypes)
isinstance('str', OldNumberTypes)

isinstance(1, NumberTypes)
```

### Bash

```bash
virtualenv venv -p python3.12
. venv/bin/activate
pip install mypy

python t.py
```
