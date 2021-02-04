# [useful interview datastructures: defaultdict (beginner - intermediate)](https://youtu.be/sunYwbKAzI0)

Today I talk about one of my favorite bits in the python collections module: defaultdict!  I also show how to write similar code without needing defaultdict if for some reason interviewers are bad and imports are banned!

## Interactive examples

### Python

```python
import collections

dct = collections.defaultdict(int)
int()
dct['a']
dct['b'] += 2
dct

dct2 = collections.defaultdict(lambda: [{}])
dct2['a']
dct2['a'].append({'foo': 'bar'})
dct2

dct3 = collections.defaultdict(int, {'a': 2, 'b': 3})
dct3['a']
```

### Bash

```bash
python t.py
```
