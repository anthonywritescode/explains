import contextlib
import timeit


def f() -> None:
    raise AssertionError('hello hello')


try:
    f()
except AssertionError:
    pass


with contextlib.suppress(AssertionError, ValueError):
    raise ValueError
    f()

setup = '''\
from contextlib import suppress
a = {"b": 2}
'''

src1 = '''\
try:
    a["c"]
except KeyError:
    pass
'''

src2 = '''\
with suppress(KeyError):
    a["c"]
'''

src3 = '''\
try:
    a["b"]
except KeyError:
    pass
'''

src4 = '''\
with suppress(KeyError):
    a["b"]
'''

print('except')
print(timeit.timeit(src1, setup=setup))

print('suppress')
print(timeit.timeit(src2, setup=setup))

print('except')
print(timeit.timeit(src3, setup=setup))

print('suppress')
print(timeit.timeit(src4, setup=setup))
