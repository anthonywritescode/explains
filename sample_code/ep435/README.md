# [assert\_never / assert\_type **CORRECTION** (intermediate)](https://youtu.be/jN_a02Rj8Gg)

I goofed in my explanation of `assert_never` during the 3.11 video -- this corrects my mistakes!

## Interactive examples

### Python

```python
import typing

typing.Never
typing.NoReturn

def f(x: typing.NoReturn) -> None: ...

def f(x: typing.Never) -> None: ...

```

### Bash

```bash
virtualenv venv -ppython3.11
. venv/bin/activate

pip install mypy

python t.py
mypy t.py
```
