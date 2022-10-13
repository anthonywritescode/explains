# [what is the "unraisable" hook (intermediate)](https://youtu.be/G4Lya0KVG1E?)

In today's video I talk about the unraisable hook, a new addition in python 3.8 and how you can use it with pytest!

## Interactive examples

### Python

```python
c = C()
c = None

import sys

def r(info):
    print(info)

sys.unraisablehook = r

c = C()
c = None
```

### Bash

```bash
python3.7 -i t.py
python -i t.py

virtualenv venv
. venv/bin/activate

pip install pytest

pytest t.py
pytest -Werror t.py
```
