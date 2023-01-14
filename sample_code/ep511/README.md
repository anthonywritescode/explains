# [python: zip and unzip (intermediate)](https://youtu.be/hOiRkFBxtpo)

Today I talk about zip, the zip footgun (and fix!), zip_longest, and unzip in python!

## Interactive examples

### Python

```python
zip
range(10)

for i in range(10):
    print(i)

ranks = list(range(1, 6))
ranks

colors = ['red', 'orange', 'yellow', 'green', 'blue']

zip(ranks, colors)
list(zip(ranks, colors))
list(zip(ranks, colors, colors))

for idx, color in zip(ranks, colors):
    print(f'{idx=} {color=}')

colors.append('violet')

ranks
colors

for idx, color in zip(ranks, colors):
    print(f'{idx=} {color=}')

for idx, color in zip(ranks, colors, strict=True):
    print(f'{idx=} {color=}')


import itertools

for idx, color in itertools.zip_longest(ranks, colors):
    print(f'{idx=} {color=}')

for idx, color in itertools.zip_longest(ranks, colors, fillvalue=-1):
    print(f'{idx=} {color=}')

list(zip(ranks, colors, colors))
lst = list(zip(ranks, colors, colors))
lst

zip(*lst)
list(zip(*lst))
list(zip(*lst))[1]
```

### Bash

```bash
python
```
