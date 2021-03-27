# [python: what are *splat **args? (intermediate)](https://youtu.be/VhDMj5ffGSc)

Today I talk about the two splat / spread operators in python!

## Interactive examples

### Python

```python
def f(x, y, z):
    print(x, y, z)

f(1, 2, 3)

lst = [1, 2, 3]
f(*lst)

f(*[], *lst)
f(*[], *lst, *[], *[])

lst.pop()
lst2 = [3]
lst
lst2
f(*lst, *lst2)

dct = {'x': 1, 'y': 2, 'z': 3}
f(x=1, y=2, z=3)
f(**dct)

f(*dct)
list(dct)
f(**dct, **{})

dct.pop('x')
dct2 = {'x': 9001}
f(**dct, **dct2)

lst
[*lst, *lst, *lst, 5, 6, 8, *lst]
(*lst, *lst, *lst, 5, 6, 8, *lst)
{*lst, *lst, *lst, 5, 6, 8, *lst}

{**dct}
{**dct, **dct}
{**dct, **dct, 'z': 9001}
```
