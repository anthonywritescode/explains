from typing import Dict
from typing import Optional


# added in python 3.x
def square(x: float, k: float) -> float:
    return x * x


# typing module was added in python3.5
def log(s: str, *, filename: Optional[str] = None) -> None:
    ...


# added in python 3.6
x: int = 5


from typing import NamedTuple

class NT(NamedTuple):
    x: int
    y: int


# added in python3.9

# old way
def print_items(dct: Dict[str, str]) -> None: ...

# def print_items(dct: dict[str, str]) -> None: ...

reveal_type(NT(1, 2).y)
