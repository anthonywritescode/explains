from typing import Generator


def gen() -> Generator[int, str, bool]:
    s = yield 1
    print(s)
    yield 2
    return False


thing = gen()
value = next(thing)
print(f'got from generator: {value}')
value2 = thing.send('hello hello')
print(f'got from generator: {value2}')
