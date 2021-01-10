# [top 10 new things in python3.9 (beginner - intermediate)](https://youtu.be/Dtw0QJhepV0)

Today I discuss and demo my top favorite new things in python3.9!

## Interactive examples

### Python

```python
# generic type annotations

from typing import Dict, List
def f(d: Dict[str, List[int]]) -> None:
    ...

dict[str, int]
def f(d: dict[str, list[int]]) -> None:
    ...

# dictionary merge operators

d1 = {1: 2, 3: 4}
d2 = {5: 6, 7: 8}
d3 = {1: 999, 999: 1}
{**d1, **d2}
d1 | d2
d1 | d3
d3
d3 |= d1
d3

# str.removeprefix / str.removesuffix

s = 'foo.exe'
s.strip('.exe')
'fooxexexe.exe'.strip('.exe')
'fooxexexe.exe'.removesuffix('.exe')
'fooxexexe.exe'.removesuffix('.exeasdf')

# ast.unparse function

import ast
module = ast.parse('x = "foo"')
ast.dump(module)
print(ast.dump(module, indent=2))
ast.unparse(module)

# new PEG parser

import contextlib
@contextlib.contextmanager
def ctx():
    yield 1

with ctx() as value:
    print(value)

with ctx() as v1, ctx() as v2:
    print(v1, v2)

with \
    ctx() as v1, \
    ctx() as v2 \
:
    print(v1,v2)

with (
    ctx() as v1,
    ctx() as v2,
):
    print(v1, v2)

# zoneinfo / graphlib modules

import zoneinfo
import graphlib
graphlib.TopologicalSorter
```

### Bash

```bash
# ppa:deadsnakes
python3.9 --version --version
python3 --version
python3 --version --version
python3.9

# line buffered sys.stderr
python3.8 line-buffered.py
python3.8 line-buffered.py |& cat

python3.9 line-buffered.py
python3.9 line-buffered.py |& cat

# __file__ of interactive scripts is absolute path
python3.8 abspath.py
python3.9 abspath.py

# curses set_tabsize / escdelay
python3.9 tabsize.py
python3.9 tabsize.py --tabsize 20

# decorators can be any expression
python3.8 decorator_expr.py
python3.9 decorator_expr.py
```
