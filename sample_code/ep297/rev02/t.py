from typing import Generator


def gen() -> Generator[int, str, bool]:
    s = yield 1
    print(s)
    yield 2
    return False


thing = gen()
value = next(thing)
reveal_type(value)
value2 = thing.send('hello hello')
reveal_type(value2)
