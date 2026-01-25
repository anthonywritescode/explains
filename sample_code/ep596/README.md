# [the python readline module is haunted](https://youtu.be/b0JQkTWjg6g)

today we explain the wacky details that broke my text editor's tests and why readline is the worst.

## Setup commands

```bash
git clone git@github.com:asottile/babi
cd babi/
```

## Interactive examples

### Python

```python
import readline
import os

os.environ['COLUMNS']
os.environ['LINES']

import subprocess
subprocess.check_call(('env',))

import readline
subprocess.check_call(('env',))

import readline
readline.__file__
```

### Bash

```bash
virtualenv venv
. venv/bin/activate
pip install -r requirements-dev.txt

pytest tests/features/go_to_line_test.py::test_prompt_window_width[tmux]
pip freeze
pip install pytest==8.3.4

python3
env -i python3

env -i python3 -c 'import subprocess; subprocess.check_call(("env",))'
env -i python3 -c 'import readline, subprocess; subprocess.check_call(("env",))'

python3
ldd <readline_file>

git rev-parse HEAD
env -i python3 t.py

nano tests/conftest.py
```
