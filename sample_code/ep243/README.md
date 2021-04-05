# [python: why object() in this code? (intermediate)](https://youtu.be/1n6kWtLrOV4)

Today I talk about a little trick utilizing object() and why you might also need the same thing!

## Interactive examples

### Python

```python
x = object()
x

y = object()
y

import sys
sys.getsizeof(x)

func({})
func({'k': None})
func({'k': ''})

func({'k': 'asdfasdf'})
func({'k': None})
```

### Bash

```bash
python -i t.py
```
