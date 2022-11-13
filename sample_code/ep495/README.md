# [securing python with audit hooks (PEP 578) (intermediate)](https://youtu.be/sIibadhDqaw)

Today I go over audit hooks -- a new feature in python 3.8 which allows one to better monitor the security sensitive parts of a python application!

## Interactive examples

### Python

```python
import sys

from typing import Any


def audit(event: str, args: tuple[Any, ...]) -> None:
    print(event, args)


sys.addaudithook(audit)
print('hi')

import subprocess
subprocess.call(('echo', 'hi'))


def audit(event: str, args: tuple[Any, ...]) -> None:
    if event == 'import' and args[0] == 'email':
        raise ImportError('no :)')


sys.addaudithook(audit)
import email

sys.modules['email']
[name for name in dir(sys) if 'audit' in name]

sys.audit('my_event_name', 1, 2, 3)
sys.addaudithook(lambda *a: print(a))
sys.audit('my_event_name', 1, 2, 3)
```

### Bash

```bash
python
```
