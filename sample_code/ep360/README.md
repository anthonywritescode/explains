# [sorting basics in python (beginner)](https://youtu.be/fqzcnd_FstY)

Today we talk about the two main ways to sort in python and everything else you need to know!

## Interactive examples

### Python

```python
x = [1, 3, 2]
x.sort()
x

sorted([1, 3, 2])
sorted((1, 3, 2))

def my_sorted(iterable, **kwargs):
    lst = list(iterable)
    lst.sort(**kwargs)
    return lst

my_sorted((1, 3, 2))

# stable sort
sorted([1, 1.])
sorted([1., 1])

sorted((3, 1, 2), reverse=True)
x.sort(reverse=True)
x

grades = {'anthony': 'A', 'jeff': 'D', 'george': 'C'}
names = ['george', 'jeff', 'anthony']

names.sort(key=lambda name: grades[name])
names

names.sort(key=lambda name: grades[name], reverse=True)
names
```

### Bash

```bash
# python3
python
```
