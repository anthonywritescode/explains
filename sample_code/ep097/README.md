# [python debugger crash course: pdb / breakpoint (beginner - intermediate)](https://youtu.be/0LPuG825eAk)

Today I go over the python debugger (pdb) and the most common commands I use!

## Setup commands

```bash
git clone git@github.com:pre-commit/pre-commit
# git clone https://github.com/pre-commit/pre-commit
cd pre-commit

virtualenv venv
. venv/bin/activate
pip install pre-commit
```

## Interactive examples

### Python

```python
import pdb; pdb.set_trace()

import pdb
pdb.set_trace()

__import('pdb').set_trace()

# python 3.7+
breakpoint()
```

### Python debugger (pdb)

```
help
continue
q  # quit

list
list .
ll  # longlist

where
up
down

locals()
globals()

ENVIRONMENT_DIR  # variable name
p ENVIRONMENT_DIR  # print

pp ret  # pretty print
p ret

n  # next
p exe
c  # continue
s  # step
p sys.executable
return
```

### Bash

```bash
pre-commit run flake8 --all-files

git diff
git add -u
git commit -m 'test'
PYTHONBREAKPOINT=0 git commit -m 'test'
```
