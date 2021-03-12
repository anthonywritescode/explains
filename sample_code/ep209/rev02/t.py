import pytest


def f(x: int) -> int:
    """silly interview question

    if it gets 4: return 7
    if it gets 7: return 4
    otherwise (unspecified)
    cannot use if statements
    """


@pytest.mark.parametrize('f', (f,))
def test_f_4(f):
    assert f(4) == 7


@pytest.mark.parametrize('f', (f,))
def test_f_7(f):
    assert f(7) == 4
