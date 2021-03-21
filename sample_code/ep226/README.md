# [python: why str('foo') (python 2 / 3 compat) (beginner - intermediate)](https://youtu.be/qNW-ITqdpfM)

Today I talk about an old technique that might appear in legacy code -- a forced native literal!  I also show how to automatically clean it up if you no longer care about python 2

## Interactive examples

### Python

```python
u'foo'
str(u'foo')
```

### Bash

```bash
python2 t.py
python3 t.py

virtualenv venv
. venv/bin/activate
pip install pyupgrade

pyupgrade --py3-plus t.py
```
