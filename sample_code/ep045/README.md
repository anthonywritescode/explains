# [typing \_\_getitem\_\_ (python / mypy) (intermediate)](https://youtu.be/HESA7oukEqE)

Today I describe how to type annotate the \_\_getitem\_\_ method for a custom sequence type using python and mypy.

## Setup commands

```bash
virtualenv venv

. venv/bin/activate

pip install mypy
```

## Interactive examples

### Python

```python
C([1, 2, 3])
c = C([1, 2, 3])
c[1]
c[1:]
```

### Bash

```bash
python -i t.py
mypy t.py
```
