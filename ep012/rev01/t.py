

class C:
    pass


def f():
    pass


for _ in range(5):
    pass


def gen():
    yield 1
    print('hello')
    yield 2
    print('world')
    yield 3


for i in gen():
    print(i)
