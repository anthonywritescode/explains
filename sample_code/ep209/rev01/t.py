

def f(x: int) -> int:
    """silly interview question

    if it gets 4: return 7
    if it gets 7: return 4
    otherwise (unspecified)
    cannot use if statements
    """


def test_f_4():
    assert f(4) == 7


def test_f_7():
    assert f(7) == 4
