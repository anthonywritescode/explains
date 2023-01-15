# [swapping without a third variable (intermediate)](https://youtu.be/NLwJI6DFF4U)

Today I show a quick math tip about swapping without a third variable -- not that you would actually do this!

## Interactive examples

### Python

```python
0 ^ 0
1 ^ 1
0 ^ 1
1 ^ 0

1 or 1
1 or 0

x = 2
y = 3

bin(x)
bin(y)

x = x ^ y
bin(x)

0 ^ 1
1 ^ 1

q = 103
bin(q)
bin(q ^ -1)
bin((q ^ -1) * -1)
bin(q ^ 0b111111111111)

bin(x)
bin(y)
y = x ^ y
bin(y)
x = x ^ y
bin(x)
bin(y)
```

### Bash

```bash
python t.py
```
