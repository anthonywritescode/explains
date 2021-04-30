# [python typing: NotImplemented is a bool? (intermediate)](https://youtu.be/5XBs_fM3Nac)

NotImplemented acts kinda strangely with python's type system -- I show how it works and why you have to be careful with it!

## Interactive examples

### Python

```python
val = eq(None)
val
isinstance(val, bool)

eq(2)
eq(2) + 5
```

### Bash

```bash
virtualenv venv
. venv/bin/activate

pip install mypy
mypy t.py

python -i t.py
```
