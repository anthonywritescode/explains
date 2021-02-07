import contextlib
from typing import Generator, Tuple


class FooError(RuntimeError):
    pass


@contextlib.contextmanager
def my_ctx() -> Generator[Tuple[int, int], None, None]:
    print('before')
    try:
        yield (42, 99)
        print('after')
    except FooError as inst:
        print(f'suppressing {inst=}')
        return True
    except BaseException as inst:
        print(f'not suppressing {inst=}')
        raise


ctx = my_ctx()
print('before ctx')
with ctx:
    print('boom')
    raise FooError('wat')
