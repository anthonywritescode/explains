# [tuple syntax doesn't have parens (beginner - intermediate)](https://youtu.be/EDGJ2TMuppM)

Today we talk about tuples in python -- and surprisingly they don't actually use parens for syntax most of the time!  I show off a little pitfall caused by this as well

## Interactive examples

### Python

```python
x = (1, 2, 3)
x

x = 1, 2, 3
x

import ast
ast.parse('x = (1, 2, 3)').body[0].value
ast.parse('x = (1, 2, 3)').body[0].value.col_offset

x = (
    1,
    2,
    3,
)

print((1, 2, 3),)
print((1, 2, 3))
print((1, 2, 3), 4)

x = ()
x

x = min(5, 4),
x

print(
    min(5, 4),
)
```

### Bash

```bash
python
```
