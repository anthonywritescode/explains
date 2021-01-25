import re
from typing import cast
from typing import Match
from typing import Optional
from typing import TypeVar


pattern = re.compile('foo')


def solution_one() -> None:
    """explicitly check the return type"""
    match = pattern.match('food')
    if match is None:
        raise AssertionError("this should have matched, why didn't it?")
    else:
        print(match.group())


def solution_two() -> None:
    match = pattern.match('food')
    assert match is not None
    print(match.group())


T = TypeVar('T')


def require_non_none(x: Optional[T]) -> T:
    if x is None:
        raise AssertionError('expected non None!')
    else:
        return x


def solution_three() -> None:
    match = require_non_none(pattern.match('food'))
    print(match.group())


def solution_four() -> None:
    match = cast(Match[str], pattern.match('food'))
    print(match.group())


solution_one()
solution_two()
solution_three()
solution_four()
