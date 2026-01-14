# [typing the untype-able with mypy plugins (advanced)](https://youtu.be/tH3Nul6jDQM)

today I show an approach to make mypy understand a very dynamic pattern with a plugin!

## Interactive examples

### Python debugger (pdb)

```
ctx
attr

ctx.type
attr

find_member
help(find_member)

import inspect
inspect.getfullargspec(find_member)

find_member.__doc__
n
find_member(attr, generic_type, generic_type)

ret = find_member(attr, generic_type, generic_type)
dir(ret)
```

### Bash

```bash
python3 t.py

virtualenv venv
. venv/bin/activate
pip install mypy

mypy t.py

python -m mypy lazy.py
python -m mypy lazy.py --show-traceback
```
