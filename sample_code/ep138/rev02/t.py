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
            print('suppressing')
            return True
        else:
            print(f'not suppressing {inst=}')
            return False


with Ctx() as (x1, x2):
    print('inside')
    print(f'{x1=} {x2=}')
