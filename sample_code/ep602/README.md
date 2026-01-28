# [python 3.14 highlights!](https://youtu.be/-Z-BDux-TRk)

it's right around the corner!  we take a look at what I think is important to know about the new release

## Interactive examples

### Python

```python
import os
print('hello hello')
wat # comment

import antigravity

import astpretty
import babi

try:
    raise AssertionError('hi')
except AssertionError, ValueError:
    print('got assertionerror or valueerror!')

try:
    raise AssertionError('hi')
except AssertionError, e:
    print(e)

thing = 'world'
t'hello {thing}'

import annotationlib

from typing import Union
Union[int | str]
int | str

from typing import Union
Union[int | str]
int | str

tp = Union[int | str]
type(tp)
type(int | str)

import compression
import compression.zstd
import compression.lzma
import compression.bz2

a, b = 1, 2, 3

import os
names = set(os.environ)

import readline
'LINES' in os.environ

os.reload_environ()
'LINES' in os.environ

new_names = set(os.environ)
new_names - names

import sys
help(sys.remote_exec)

import operator
operator.is_none
operator.is_not_none
operator.is_not_none(None)

import ast
ast.compare
ast.parse('import os\n\nimport sys')
ast.parse('import os\n\nimport sys') == ast.parse('import os\n\nimport sys')

ast.compare(ast.parse('import os\n\nimport sys'), ast.parse('import os\n\nimport sys'))
ast.compare(ast.parse('import os\n\nimport sys'), ast.parse('import os\n\nimport sys'), compare_attributes=True)
ast.compare(ast.parse('import os\n\nimport sys'), ast.parse('import os\nimport sys'), compare_attributes=True)

print(list(zip((1, 2, 3), (1, 2), strict=True)))
print(list(zip((1, 2, 3), (1, 2))))

list(map(print, (1, 2), (3, 4, 5)))
list(map(print, (1, 2), (3, 4, 5), strict=True))

import concurrent.futures
concurrent.futures.InterpreterPoolExecutor
```

### Bash

Sesion 1:

```bash
sudo add-apt-repository ppa:deadsnakes
# OR
sudo add-apt-repository ppa:deadsnakes/nightly

python3.14

python3.14 -m json t.json
python3.14 -m json t.json --help
python3.14 -m json --compact t.json

python3.14 -m calendar

python3.14 argparse_example.py
python3.14 argparse_example.py --help

python3 -m argparse_example --help
mkdir argparse_example
touch !$/__init__.py
mv argparse_example.py argparse_example/__main__.py
python3 -m argparse_example --help
python3.14 -m argparse_example --help

python3.14
virtualenv venv -ppython3.14
. venv/bin/activate

pip install babi
pip install astpretty
python

docker run --rm -ti python:2-slim bash
python

python3.14 t-string-demo.py

python3.13 t.py
python3.14 t.py
python3.14 -m dis t.py

python3.13
python3.14

ps -ef | grep babi
python3.14 -m pdb -p <pid>
gdb venv/bin/python3 -p <pid>
sudo gdb venv/bin/python3 -p <pid>

ps -ef | grep bot
sudo python3.14 -m asyncio ps <pid>
sudo python3.14 -m asyncio pstree <pid>
```

Session 2:

```bash
babi

virtualenv venv314 -ppython3.14
./venv314/bin/pip install -r requirements.txt
./venv314/bin/python3 -m bot
```
