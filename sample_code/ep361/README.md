# [multiplying str / list / tuple and pitfalls (beginner - intermediate)](https://youtu.be/ZFjV3M-xl_M)

Today I talk about some nifty operator overloading in python for multiplication and why you have to be careful with it sometimes!

## Interactive examples

### Python

```python
5 * 5

'a' * 5
'asdf' * 5

print('=' * 79)

[1] * 10
(1,) * 10

lst = [[0]] * 10
lst[0].append(2)
lst

lst = [[0] for _ in range(10)]
lst
lst[0].append(2)
lst

tup = ([0],) * 10
tup
tup[0].append(2)
tup

tup = tuple([0] for _ in range(10))
tup
tup[0].append(2)
tup
```

### Bash

```bash
# python3
python
```
