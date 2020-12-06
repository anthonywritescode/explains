def square(n: int) -> int:
    return n * n


def test_square_1():
    assert square(1) == 1


def test_negative_square_1():
    assert square(-1) == 1


def test_square_2():
    assert square(2) == 4
