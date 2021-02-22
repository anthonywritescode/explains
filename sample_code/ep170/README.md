# [python typing: Literal (intermediate)](https://youtu.be/ZHisrvgF1Wk)

Today we talk about the `Literal` type in python and how it can help make overloading easier

## Interactive examples

### Python

```python
import subprocess
subprocess.check_output(('echo', 'hi'))
subprocess.check_output(('echo', 'hi'), text=True)
```

### Bash

```bash
python t.py

virtualenv venv
. venv/bin/activate
pip install mypy

mypy t.py
```
