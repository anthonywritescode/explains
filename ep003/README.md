# [my favorite python str method! (beginner - intermediate)](https://youtu.be/kx6G3nkZTjM)

Oops spoiler in the thumbnail it's str.partition, oh well -- I explain my favorite string method and show some toy examples where it's useful -- maybe this will help you manipulate strings too!

## Interactive examples

### Python

```python
x = 'hello world'
type(x)
dir(str)
sorted(['pytest-cov', 'pytest'])

s = 'hello world'
s.partition('==')
s.partition(' ')

f1 = 'foo.txt'
f2 = 'foo.bar.txt'
f3 = 'Dockerfile'
import os.path
os.path.splitext(f1)
os.path.splitext(f2)
os.path.splitext(f3)

def to_extension(s):
    _, _, ext = s.rpartition('.')
    return ext

to_extension(f1)
to_extension(f2)
to_extension(f3)

s = 'hello world'
s.rpartition('.')
s.partition('.')

s.partition(' ')
s.rpartition(' ')

s = 'hello world anthony!'
s.rpartition(' ')
s.partition(' ')
```
