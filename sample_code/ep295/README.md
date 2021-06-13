# [date.today() is twice as slow as datetime.now().date()??? (intermediate)](https://youtu.be/PBg6EorsX7s)

Today we take a look at `date.today()` and `datetime.now().date()` and figure out why it's so much slower -- then we speed it up!

## Setup commands

```bash
git clone git@github.com:python/cpython
# git clone https://github.com/python/cpython
cd cpython
```

## Interactive examples

### Bash

```bash
python3.10 -m timeit -s 'from datetime import date' 'date.today()'
python3.10 -m timeit -s 'from datetime import datetime' 'datetime.now().date()'

nano Modules/_datetimemodule.c
git apply patch # https://bugs.python.org/issue44307
git diff -w
make -j 5

./python -m timeit -s 'from datetime import datetime' 'datetime.now().date()'
./python -m timeit -s 'from datetime import date' 'date.today()'
```
