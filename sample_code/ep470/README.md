# [why does python think -1\*\*0 is -1 ? (intermediate)](https://www.youtube.com/watch?v=T49G4WwmvnA)

Today I show how even if you don't know the operator precedence you can figure out how this evaluates!

## Interactive examples

### Python

Session 1:

```python
6 ** 0
109238091823 ** 0
0 ** 0

-1 ** 0
(-1) ** 0
```

Session 2:

```python
-(1**0)
1**0
-(1)
```

### Bash

```bash
virtualenv venv
. venv/bin/activate

pip install astpretty
astpretty /dev/stdin <<< '-1 ** 0'
astpretty /dev/stdin --no-show-offsets <<< '-1 ** 0'
```
