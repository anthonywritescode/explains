# [@staticmethod / @classmethod (beginner + advanced)](https://youtu.be/yhkpRz7TC7o)

Today I walk through what the `staticmethod` and `classmethod` decorators do -- I also show roughly how to implement them as descriptor classes

## Interactive examples

### Python

```python
C.f()
C().f()

C.g()
C().g()
```

### Bash

```bash
python -i t.py
all-repos-grep 'def __get__' -- '*.py'
```
