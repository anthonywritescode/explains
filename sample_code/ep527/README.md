# [tuples! (and their syntax quirks) (beginner)](https://youtu.be/J3-tL6OnFWA)

Did you know that it isn't the parentheses that make a tuple?

## Interactive examples

### Python

```python
()

x = ()
len(x)
x[0]

(1,)
1,

print((1,))
print(1,)

1, 2, 3, 4
(1, 2, 3, 4)
(1)
(1,)

tuple('asdfasdf')
(1, 2, *[4, 5, 6])
x = (4, 5, 6)
(1, 2, *x)

(1, 2) + (3, 4)
2 in (1, 4, 7)
4 in (1, 4, 7)

x = (1, 2, 3)
x[1] = 2

x = ([0], [2], [4])
x[0].append(1)
x
x[0] += [2]

{(1, 2): 'hello'}

()
(1)
1,
(1,)
```

### Bash

```bash
python
python -m pydoc tuple
```
