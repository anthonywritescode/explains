# [ONE TERABYTE of RAM saved with a single line of code (advanced)](https://youtu.be/Hgw_RlCaIds)

Today I show off a small change I made at work with huge impact and explain how it works!

## Setup commands

```bash
git clone git@github.com:python/cpython
# git clone https://github.com/python/cpython

cd cpython
```

## Interactive examples

### Python

```python
import gc
gc.freeze()
```

### Bash

```bash
git grep 'typedef .* PyObject;'
git grep 'struct _object'
nano Include/object.h
```
