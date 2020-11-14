# [what's wrong with python's blank except:? (beginner - intermediate)](https://youtu.be/i0GOLe-F27Q)

The dreaded "E722 do not use bare 'except'"! Today we explain the various ways to "catch all exceptions" as well as some recommendations on how to properly fix this problem!

## Setup commands

```bash
virtualenv venv

. venv/bin/activate

pip install flake8
```

## Interactive examples

### Python

```python
# python 3
Exception.__bases__
BaseException.__bases__
BaseException.__subclasses__()
```

### Bash

```bash
echo hello world > dne
# echo 'hello world' > dne

flake8 t.py
flake8 --help | less
```
