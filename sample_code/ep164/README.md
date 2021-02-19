# [structural subtyping in python with Protocol! (intermediate)](https://youtu.be/QjFChmQHJxk)

Today I talk about one of my favorite additions to typing: Protocol!  in this we extend from a previous example where we used overload to more-properly support any `__index__`-able type!

## Interactive examples

### Python

```python
class C:
    def __index__(self) -> int:
        return 3

foo = b'foooooo'
foo[3]
foo[C()]

(4).__index__()
```

### Bash

```bash
virtualenv venv
. venv/bin/activate
pip install mypy

python t.py
mypy t.py

git grep Protocol
```
