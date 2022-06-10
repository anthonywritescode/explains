from typing import Sequence


def is_list_of_strings(lst: Sequence[object]) -> bool:
    return isinstance(lst, list) and all(isinstance(x, str) for x in lst)


def f(x: list[str] | list[int]) -> None:
    if is_list_of_strings(x):
        print(f'got commands {" ".join(x)}')
    else:
        print(f'got numbers: {" ".join(str(y) for y in x)}')
