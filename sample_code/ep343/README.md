# [why does id(float(1)) == id(float(2)) ??? (intermediate)](https://youtu.be/jjm10-Ug1aE)

Today we explain a bit of an oddity with `id(...)` in cpython and explain why two separate objects can have the same id!

## Interactive examples

### Python

```python
id
help(id)

id(1)
id(2)
id(3)
id(1)

x = 123.123
id(x)
id(x)

id(float(1)) == id(float(2))
id(float(1))
id(float(2))


class C():
    def __init__(self):
        print(f'__init__: {id(self)}')
    def __del__(self):
        print(f'__del__: {id(self)}')


id(C())
print(id(C()))

id(C()) == id(C())
```

### Bash

```bash
python -mpydoc id
pypy3
```
