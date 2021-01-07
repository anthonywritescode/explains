# [what is the underscore (\_) for? (beginner)](https://youtu.be/VKz1aQbNnyI)

Today I talk about the three main places you'll see an underscore (and even a double-underscore!) in python

## Setup commands

```bash
git clone git@github.com:pre-commit/pre-commit
# git clone https://github.com/pre-commit/pre-commit
cd pre-commit
```

## Interactive examples

### Python

```python
5 ** 30
x = _
x
5 ** 20
print(f'the previous result was {_}')

_ = 123
_

person = ('Anthony', 29, 'San Mateo, CA')
name, _, location = person
_, _, location = person
*_, location = person

def f(*_, **__):
    print('hi')

f()
f(1)
f(1, a=1)
f(1, a=1, b=2)

def f(*_, **_): pass

```
