# [what is a .pth file? (intermediate)](https://youtu.be/mzxQrgvuRFg)

Today I talk about `.pth` files in python and how they can influence python startup!

## Interactive examples

### Notes

```text
1. ignore comments (#)
2. if it starts with `import ` => exec that line
3. otherwise add thing to sys.path
```

### Python

```python
import sys
sys.path

import t
import pyupgrade
pyupgrade.__file__
```

### Bash

```bash
virtualenv venv
. venv/bin/activate

ls venv/lib/python*/site-packages/*.pth

python
python -c ''
python -c '' && python -c ''
mkdir y

pip install -e ~/workspace/pyupgrade

virtualenv venv2 -p python2
. venv2/bin/activate
python t.py
pip install future-fstrings
python t.py
future-fstrings-show t.py
```
