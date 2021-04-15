# [python easter eggs: \_\_peg\_parser\_\_ (beginner)](https://youtu.be/p985PaTjqlc)

Today I talk about an easter egg, or should I call it an easter PEG that's only in python 3.9!

## Setup commands

```bash
git clone git@github.com:python/cpython
# git clone https://github.com/python/cpython
cd cpython
```

## Interactive examples

### Python

```python
print('hello')

import contextlib

with (contextlib.nullcontext(), contextlib.ExitStack() as ctx):
    pass

with (contextlib.ExitStack() as ctx1, contextlib.nullcontext() as ctx2):
    pass

__peg_parser__
__new_parser__
```

### Bash

```bash
python3.9 -Xoldparser
python3.9

git log --oneline -G peg_parser -- '*.c'
git show c5fc156852
```
