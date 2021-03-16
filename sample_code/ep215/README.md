# [python easter eggs: easiest hello world! (beginner)](https://youtu.be/ViNc-g60br8)

My only complaint is that it isn't "hello hello world" -- today I talk about the `__hello__` module -- one of the oldest in cpython!

## Setup commands

```bash
git clone git@github.com:python/cpython
# git clone https://github.com/python/cpython

cd cpython
```

## Interactive examples

### Python

```python
import __hello__
__hello__

import dis
dis.dis(__hello__)
```

### Bash

```bash
python -m __hello__
git show <commit_hash>

python -c 'import __phello__'
python -c 'import __phello__.spam'

git log -G __phello__ -- Python/frozen.c
```
