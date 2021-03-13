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


@pytest.mark.parametrize(
    'f',
    (
        f_ternary,
        f_old_ternary,
    ),
)
def test_f_4(f):
    assert f(4) == 7


@pytest.mark.parametrize(
    'f',
    (
        f_ternary,
        f_old_ternary,
    ),
)
def test_f_7(f):
    assert f(7) == 4
