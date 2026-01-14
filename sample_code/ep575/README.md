# [`x: float = False` is a valid annotation??? (intermediate)](https://youtu.be/RYD87EL1Zbs)

today we talk a bit about the numeric tower in mypy's type system and a few quirks that result from it.

## Setup commands

```bash
virtualenv venv
. venv/bin/activate
pip install mypy
```

## Interactive examples

### Python

```python
isinstance(False, float)
isinstance(NotImplemented, float)

isinstance(1, float)
isinstance(False, int)

False + False
True + True

NotImplemented
type(NotImplemented).__bases__
NotImplemented + 1

(1.5).as_integer_ratio()
(1).as_integer_ratio()
(1).as_integer()
```

### Bash

```bash
mypy t.py
python3
```
