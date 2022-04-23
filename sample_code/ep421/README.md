# [repr(...) doesn't work the way you expect (intermediate - advanced)](https://youtu.be/e3bqdxqLvH4)

Today I show a little quirk of `repr` and how it doesn't quite act like `__repr__`!

## Interactive examples

### Python

```python
exit

exit.__repr__ = lambda self: exit()
exit

type(exit).__repr__ = lambda self: exit()
exit

exit.__dict__
type(exit).__dict__

repr(D())

myrepr(C())
myrepr(D())
```

### Bash

```bash
python -i t.py
```
