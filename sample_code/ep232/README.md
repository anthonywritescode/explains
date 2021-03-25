# [the 2 modes of python's str.split (beginner)](https://youtu.be/6pIPMHP2Lwg)

Today I show how `str.split` works (and how it oddly has two quite-different modes of execution)

## Interactive examples

### Python

```python
'foo bar baz'.split(' ')
'foo  bar  baz'.split('  ')
'foo  bar baz'.split('  ')
'foo  bar baz  '.split('  ')

'foo  bar baz  '.split()
'  foo  bar baz  '.split()
'  foo  bar baz  '.split('  ')

'  foo  bar \t \n \f baz  '.split()

def split_like_no_arg(s, split_str):
    lst = s.split(split_str)
    if s.endswith(split_str):
        lst.pop()
    if s.startswith(split_str):
        lst.pop(0)
    return lst

split_like_no_arg('  foo  bar  baz  ', '  ')
split_like_no_arg('  foo  bar  baz ', '  ')
split_like_no_arg('  foo  bar  baz  a', '  ')

''.split('  ')
''.split()
```
