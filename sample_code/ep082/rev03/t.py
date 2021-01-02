from typing import Tuple
from typing import Type
from typing import Union


ExcType = Union[
    Type[BaseException],
    Tuple[Type[BaseException], ...],
]


def catch_these(tp: ExcType) -> None:
    try:
        raise AssertionError('hello')
    except tp as e:
        print(f'caught {tp}: {e}')
    except Exception:
        print(f'not caught: {tp}')


catch_these(TypeError)
catch_these(AssertionError)
catch_these((TypeError, AssertionError))

# except (TypeError, AssertionError) as e:
