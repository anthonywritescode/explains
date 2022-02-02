# [python: what is 0-arg raise? (beginner)](https://youtu.be/yj4z1N3_0sw)

Today we talk a bit about the `raise` statement and how it works if you don't specify any exception

## Interactive examples

### Python

```python
mkdirp('foo/bar')

import sys
sys.exc_info()

[attr for attr in dir(sys) if 'exc' in attr]

import dis
dis.dis(mkdirp)
```

### Bash

```bash
python -m pydoc os.makedirs

touch foo

python -i t.py
```
