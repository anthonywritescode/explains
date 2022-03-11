# [how to modify a list while iterating (intermediate)](https://youtu.be/JXis-BKRDFY)

*normally* you can't modify a list while iterating over it but I show a little trick that makes it possible.  I also show how you might refactor "iterating a dict while modifying" as well!

## Interactive examples

### Python

```python
lst = list(range(10))
it = iter(lst)

next(it)
lst.remove(0)
next(it)

dct = {v: v for v in range(10)}
dct

for k, v in dct.items():
    if k == 2:
        del dct[k]
```

### Bash

```bash
python t.py
```
