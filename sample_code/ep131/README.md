# [python: len(x) vs x.\_\_len\_\_() (beginner - intermediate)](https://youtu.be/KyqiduLIL5k)

Today I talk about the difference between `len(x)` and `x.__len__()` (as well as other similar functions!)

## Interactive examples

### Python

```python
class C:
    def __len__(self) -> int:
        return 3

len
help(len)

len(C())
C().__len__()
repr(C())

class D:
    def __len__(self):
        return 'hello hello world'

D().__len__()
len(D())

class E:
    def __len__(self):
        return '5'

len(E())
```
