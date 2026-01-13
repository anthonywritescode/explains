# [python 3.13 release highlights](https://youtu.be/gqqgwyNx52Q)

it's just around the corner!  I walk through the things that I think are noteworthy / I'm excited about in python 3.13!  don't worry not too much typing stuff this time smile.

## Interactive examples

### Python

```python
exit

def foo():
    print('hello world')

import itertools
help(itertools.batched)

import inspect, first_line_no
inspect.getsource(first_line_no.C)
inspect.getsource(first_line_no.D)
inspect.getsource(first_line_no.E)

C.__firstlineno__
D.__firstlineno__
E.__firstlineno__

f.__doc__
import inspect
inspect.getdoc(f)

f.__doc__

C.__static_attributes__
D.__static_attributes__

D.mro()
[cls.__static_attributes__ for cls in D.mro() if hasattr(cls, '__static_attributes__')]
[attr for cls in D.mro() if hasattr(cls, '__static_attributes__') for attr in cls.__static_attributes__]
{attr for cls in D.mro() if hasattr(cls, '__static_attributes__') for attr in cls.__static_attributes__}

help(C)

import os
os.cpu_count()
os.process_cpu_count()

import types
types.SimpleNamespace(foo=1, bar=2)
obj = types.SimpleNamespace(foo=1, bar=2)
obj.foo

types.SimpleNamespace({'foo': 1, 'bar': 2})
types.SimpleNamespace(**{'foo': 1, 'bar': 2})

import copy
copy.replace

import datetime
now = datetime.datetime.now()
now
now.replace(year=2025)

import collections
nt = collections.namedtuple('nt', ('a', 'b'))
nt(a=1, b=2)

obj2 = nt(a=1, b=2)
obj2._replace(b=3)

obj2.__replace__(b=3)
copy.replace(obj2, b=3)
```

### Bash

```bash
python3.12 free-threaded-demo.py
python3.13 free-threaded-demo.py

# add the deadsnakes ppa first
# sudo apt install python3.13-nogil
python3.13t free-threaded-demo.py

python3.13
python3.12
PYTHON_BASIC_REPL=1 python3.13

python3.13 traceback-example.py
python3.13 traceback-example.py |& cat

python3.12 pdb-example.py
python3.13 pdb-example.py

python3.12 random.py
python3.13 random.py

python3.12 astpretty.py
python3.13 astpretty.py

virtualenv venv
ls venv/ -al
rm -rf venv/

python3.13 -m venv venv
ls venv/ -al

python3 -m pydoc os
time PAGER=false python3.12 -m pydoc test.test_enum
time PAGER=false python3.13 -m pydoc test.test_enum

python3.12
python3.13 -i first_line_no.py
python3.13

python3.12 -i doc_string_example.py
python3.13 -i doc_string_example.py

python3.13 -i static_attributes_example.py

python3.9 classmethod_deprecation.py
python3.8 classmethod_deprecation.py

python3.10 -i classmethod_deprecation.py
python3.11 -Werror classmethod_deprecation.py
python3.12 -Werror classmethod_deprecation.py
python3.13 -Werror classmethod_deprecation.py

npm i pyright
./node_modules/.bin/pyright typevar-defaults.py --pythonversion 3.13

python3.13 t.py

python3.13 -m random foo bar baz
python3.13 -m random 123
python3.13 -m random 123.123
python3.13 -m random --help

python3.13 argparse_deprecated_option.py --old-option val
python3.13
```
