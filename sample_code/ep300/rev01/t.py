import pytest


def square(x: float) -> float:
    return x * x


@pytest.mark.parametrize(
    ('n', 'expected'),
    (
        (0, 0),
        (5, 25),
    )
)
def test_square(n, expected):
    assert square(n) == expected
