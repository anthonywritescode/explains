# [NotImplemented vs NotImplementedError (beginner - intermediate)](https://youtu.be/GSBqmYUnBdk)

Today I go over the easily confusable NotImplemented and NotImplementedError -- as well as covering functools.total_ordering -- a very helpful tool for implementing comparisons (did you know you can derive all comparison operators from just less-than?)

## Interactive examples

### Python

```python
C(1)
D(2)

C(1) < D(2)

C(1) < C(2)
C(1) < C(0)
C(1) < D(2)

x = 1
y = 1
not (x < y) and not (y < x)

y = 2
not (x < y) and not (y < x)

C(1) < D(2)
```

### Bash

```bash
python -i t.py
```
