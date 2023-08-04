# [python 3.12 release highlights (beginner - advanced)](https://youtu.be/IV8OZY4194U)

It's here!  with ugly new typing syntax and infinitely nestable fstrings and one of the funniest changes I've seen in a while -- python 3.12!

## Interactive examples

### Python

```python
import calendar
calendar.January
calendar.February
calendar.March

hi = 3
f'hi{f'{hi}'}'

f'hi{
3
}'

f'hi{
  3  # hi
}'

Old = int
isinstance(5, Old)

type Newest = int
isinstance(5, Newest)
Newest.__value__

import dis

def f():
    x = [i * 2 for i in range(5)]
    return x

dis.dis(f)

'\d'
r'\d'
'\\d'

it = [1, 2, 3, 4, 5, 6, 7, 8, 9]

import itertools

for a, b, c in itertools.batched(it, 3):
    print(a, b, c)

for a, b in itertools.batched(it, 2):
    print(a, b)

sys.version_info

class C:
    def __init__(self):
        self.x = 1
    def f(self):
        x

C().f()

import Counter from collections

from collections import counter
```

### Python debugger (pdb)

```
$x = 1
import token
$token = token
$token

y = 1
c
y

q
```

### Bash

```bash
python3.11
python3.12
python3.12 -m pydoc tokenize

cd pre-commit/
best-of -n 5 python3.11 t.py $(git ls-files -- '*.py')
best-of -n 5 python3.12 t.py $(git ls-files -- '*.py')

python3.11 -m tokenize /dev/stdin <<< 'f"hello {world}"'
python3.12 -m tokenize /dev/stdin <<< 'f"hello {world}"'
python3.12 -m tokenize /dev/stdin <<< 'f"{a}({world})"'

python3.12 -m venv vvv
sudo apt install python3.12-venv

virtualenv venv -ppython3.12
./venv/bin/pip freeze --all
./venv/bin/pip install setuptools
./venv/bin/python3 -c 'import distutils'

. venv/bin/activate
pip install pycodestyle
pycodestyle t4.py

pip install pyupgrade
cat t4.py

pyupgrade t4.py
cat t4.py

cd pyflakes
deactivate

python3.12 -m unittest discover pyflakes
python3.12 -m unittest discover pyflakes --duration 5
python3.12 -m unittest discover pyflakes --duration 10
```
