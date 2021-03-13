import pytest

"""silly interview question

if it gets 4: return 7
if it gets 7: return 4
otherwise (unspecified)
cannot use if statements
"""


def f_ternary(x: int) -> int:
    return 4 if x == 7 else 7


def f_old_ternary(x: int) -> int:
    return 4 if x == 7 else 7


def f_dict(x: int) -> int:
    return {4: 7, 7: 4}[x]


f_dict2 = {4: 7, 7: 4}.__getitem__


def f_list(x: int) -> int:
    return [0, 0, 0, 0, 7, 0, 0, 4][x]


def f_addition(x: int) -> int:
    return 11 - x


def f_bitflip(x: int) -> int:
    return x ^ 0b11


FUNCS = pytest.mark.parametrize(
    'f',
    (
        f_ternary,
        f_old_ternary,
        f_dict,
        f_dict2,
        f_list,
        f_addition,
        f_bitflip,
    ),
)


@FUNCS
def test_f_4(f):
    assert f(4) == 7


@FUNCS
def test_f_7(f):
    assert f(7) == 4
