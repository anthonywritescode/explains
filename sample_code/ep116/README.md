# [python: .sort() vs sorted(...) (beginner - intermediate)](https://youtu.be/JZYWtmxaCeM)

Today I talk about the difference between list.sort() and sorted(iterable) and when you should pick one over the other (I also show how sorted(...) works under the hood!)

## Interactive examples

### Python

```python
lst = [1, 5, 34, 2]
lst
lst.sort
lst.sort()

sorted([1, 5, 34, 2])
lst = [1, 5, 34, 2]
lst2 = sorted(lst)
lst
lst2

sorted((1, 5, 4))

def f():
    yield 1
    yield 5
    yield 4

sorted(f())

def my_sorted(it):
    lst = list(it)
    lst.sort()
    return lst

my_sorted((1, 5, 4))
my_sorted(f())
```
