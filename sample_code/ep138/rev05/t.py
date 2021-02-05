import sys
from types import TracebackType
from typing import Tuple
from typing import Type
from typing import Optional


class FooError(RuntimeError):
    pass


class Ctx:
    def __init__(self) -> None:
        print('initialization')

    def __enter__(self) -> Tuple[int, int]:
        print('before')
        return (42, 99)

    def __exit__(
            self,
            tp: Optional[Type[BaseException]],
            inst: Optional[BaseException],
            tb: Optional[TracebackType],
    ) -> Optional[bool]:
        print('after')

        if isinstance(inst, FooError):
            print(f'suppressing {inst=}')
            return True
        else:
            print(f'not suppressing {inst=}')
            return False


ctx = Ctx()
print('before ctx')

__enter__ = type(ctx).__enter__
__exit__ = type(ctx).__exit__

try:
    print('boom')
    raise RuntimeError('wat')
except BaseException:
    suppressed = __exit__(ctx, *sys.exc_info())
    if not suppressed:
        raise
else:
    __exit__(ctx, None, None, None)
