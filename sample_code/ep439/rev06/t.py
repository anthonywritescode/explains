from typing import Sequence
from typing import TypeGuard


def is_list_of_strings(lst: Sequence[object]) -> TypeGuard[list[str]]:
    return isinstance(lst, list) and all(isinstance(x, str) for x in lst)


def f(x: list[str] | list[int]) -> None:
    if is_list_of_strings(x):
        reveal_type(x)
        print(f'got commands {" ".join(x)}')
    else:
        print(f'got numbers: {" ".join(str(y) for y in x)}')
