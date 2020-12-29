# [generator basics (+typing) (beginner - intermediate)](https://youtu.be/LjBa9sfJh7U)

Today I talk about the basics of generator functions and how you'd type annotate them!

## Setup commands

```bash
virtualenv venv
. venv/bin/activate
pip install mypy
```

## Interactive examples

### Python

```python
import t
for thing in t.my_range(10):
    print(thing)

gen = t.my_range(10)
gen
next(gen)
next(gen)
next(gen)
next(gen)

gen = t.my_range(10)
while True:
    try:
        value = next(gen)
    except StopIteration:
        break
    else:
        print(value)

list(range(10))

import t
for x in t.my_range(10):
    print(f'got x: {x}')
```

### Bash

```bash
python t.py
```
