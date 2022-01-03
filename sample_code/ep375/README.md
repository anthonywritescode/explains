# [python: what is `__file__`? (beginner - intermediate)](https://youtu.be/LVhxqOznPg0)

Today I show `__file__` and how you can use it to find files relative to python scripts / modules!

## Interactive examples

### Python

```python
import flask
flask.__file__

import _onigurumacffi
_onigurumacffi.__file__

import _cffi_backend
_cffi_backend.__file__

import t2
t2.__file__
```

### Bash

```bash
mkdir t2

python3.8 t.py
python3.8 $PWD/t.py

python3.9 t.py
python3.9 $PWD/t.py

echo $PWD

# git clone https://github.com/anthonywritescode/aoc2021
git clone git@github.com:anthonywritescode/aoc2021
cd aoc2021/
nano support/support.py

virtualenv venv
. venv/bin/activate

pip install flask
pip install onigurumacffi

ls venv/lib/python*/site-packages/*.so
```
