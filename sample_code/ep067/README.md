# [python: Ellipsis (...) and typing (beginner - intermediate)](https://youtu.be/yLwvOwTO068)

Today I talk about the Ellipsis builtin and how it made its way to being a first class citizen as well as its applications in typing / mypy.

## Setup commands

```bash
virtualenv venv

. venv/bin/activate

pip install mypy
```

## Interactive examples

### Python

Session 1:

```python
Ellipsis
x = Ellipsis
x
True
None
False
...

def f(): ...

# def f(): pass

def f(): 5

(lambda: None).__name__
```

Session 2:

```python
...

class C:
    def __getitem__(self, obj):
        self.x = obj

c = C()
c[...]
c.x
Ellipsis
```

### Bash

```bash
mypy t.py
```
