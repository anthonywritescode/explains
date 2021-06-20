from typing import Generator


def gen() -> Generator[int, str, bool]:
    s = yield 1
    print(s)
    yield 2
    print('about to end')
    return False


thing = gen()
value = next(thing)
print(f'got from generator: {value}')
value2 = thing.send('hello hello')
print(f'got from generator: {value2}')

try:
    next(thing)
except StopIteration as e:
    ret, = e.args
    print(f'got this out of exception: {ret}')
