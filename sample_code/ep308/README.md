# [gradual typing python (and my approach) (beginner - intermediate)](https://youtu.be/Rk-Y71P_9KE)

Today I talk about gradual typing, what that means for mypy, and the settings I tend to use when I'm adding types to a codebase

## Interactive examples

### Bash

```bash
virtualenv venv
. venv/bin/activate
pip install mypy

mypy t.py
mypy --check-untyped-defs t.py

nano setup.cfg
```
