# [quick debugging tool: python -i (beginner)](https://youtu.be/B4wkrdcc28A)

Today I talk about a quick debugging technique for python via `-i` and show a few examples of how to use it!

## Interactive examples

### Python

```python
dir()
_lt(10)
_lt(100)
_lt(124)

_gt(20)
_gt(24)

import ast
pprint(ast.parse("x = 1"))
```

### Bash

```bash
# git clone https://github.com/asottile/covdefaults
git clone git@github.com:asottile/covdefaults
cd covdefaults

tox --devenv venv
. venv/bin/activate

# python3 -i covdefaults.py
python -i covdefaults.py
python -i -m covdefaults

deactivate
cd ..

# git clone https://github.com/asottile/astpretty
git clone git@github.com:asottile/astpretty
cd astpretty/

# python3 -i -m aspretty
python -i -m aspretty
```
