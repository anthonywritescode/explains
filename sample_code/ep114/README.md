# [python: comma, = assignment! (beginner - intermediate)](https://youtu.be/WLKi_gPKCp0)

Today I talk about the 1-ary unpacking assignment and an example and why it's useful!

## Interactive examples

### Python

```bash
x = [1]
y, = x
y

x, y = [1, 2]
x
y

(x,) = [1]
x

()
x, = [1]

y = [1]
x = y[0]
x

y.append(3)
y
x = y[0]
x, = y
```

### Bash

```bash
python t.py
```
