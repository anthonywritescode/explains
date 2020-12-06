# [python type(x).\_\_name\_\_ vs x.\_\_class\_\_.\_\_name\_\_ (intermediate)](https://youtu.be/6rAIttnm3Fs)

Very short one, I explain why I prefer `type(x).__name__` vs `x.__class__.__name__`.  thanks to @alikus for the question!

## Interactive examples

### Python

```python
# python3.8
Location()
class C:
    @property
    def __class__(self):
        print('return custom type')
        return int

C().__class__
C().__class__.__name__
type(C())


# python2.7
class Old: pass
class New(object): pass

old = Old()
new = New()
type(new).__name__
type(old).__name__
type(old)
```

### Bash

```bash
python3.8 -i t.py
# older version of python
python2.7 -i t.py
```
