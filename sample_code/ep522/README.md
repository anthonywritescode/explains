# [how do virtualenvs actually work (advanced)](https://youtu.be/XFqDHPYfTwE)

Today I go over the technical details of how virtualenvs actually function, including the absurdity of needing to start 3 processes for every executable on windows

## Interactive examples

### Notes

```text
babi.exe
----> python.exe (in the virtualenv)
--------> python.exe (C:\Python310\python.exe)


(normal executable code)
byte marker [4 bytes]
#!python.exe
zip file
=>
    __main__.py
        from babi import main
        sys.exit(main())


venv310\Scripts\python.exe venv310\Scripts\babi.exe
```

### Python

```python
import sys

sys.executable
sys.prefix
sys.base_prefix
sys.path

# Windows

import os
os.environ['__PYVENV_LAUNCHER__']

import psutils
procs = [proc for proc in psutil.process_iter() if 'python' in proc.name()]
procs
procs[0].environ()['__PYVENV_LAUNCHER__']

import sys
sys.path
sys.prefix
sys.base_prefix

import psutils
procs = [proc for proc in psutil.process_iter() if 'babi' in proc.name()]
child1 = procs[0].children()
child1[0].exe()

procs[0].children()[0].children()
procs[0].children()[0].children()[0].exe()

import zipfile
zipf = zipfile.ZipFile(r'venv310\Scripts\babi.exe')
zipf.namelist()
zipf.open('__main__.py').read()

# print(zipf.open('__main__.py').read().decode())
```

### Bash

```bash
virtualenv venv
tree -L 2 venv

ls /usr/lib/python3*
ls venv/bin/python3 -al
ls venv/bin/python -al

venv/bin/python
./venv/bin/pip install astpretty

ls venv/lib/python3*/site-packages
ls venv/bin/

head -1 venv/bin/astpretty

./venv/bin/astpretty /dev/stdin <<< '1 + 1'
```

### Windows CMD

```batch
: python virtualenv.pyz venv310
ls venv310
ls venv310\Lib
ls venv310\Scripts

ls venv310\Scripts\python.exe
ls -al venv310\Scripts\python.exe

du -hs venv310\Scripts\python.exe
du -hs C:\Python310\python.exe

ls venv310\pyvenv.cfg
cat venv310\pyvenv.cfg

venv310\Scripts\python.exe
```
