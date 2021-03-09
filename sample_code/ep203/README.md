# [python is compiled? (+ disassembler) (intermediate)](https://youtu.be/FPJdre3mbD4)

Python is compiled to a lower-level byte code and then executed in a stack-based virtual machine!  today I go over some basics of the low level VM and show off the disassembler

## Interactive examples

### Python

```python
repr(print('hello'))

import dis
def f():
    print('hello hello' + 'world')

dis.dis(f)
```

### Bash

```bash
python t.py

python -c 'import t'
ls
ls __pycache__/
file __pycache__/t.cpython-*.pyc

python -m dis t.py
```
