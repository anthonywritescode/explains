import pytest


def square(n: int) -> int:
    return n * n


@pytest.mark.parametrize(
    ('input_x', 'expected'),
    (
        (1, 1),
        pytest.param(-1, 1),
        pytest.param(-1, 1, id='negative trivial case'),
        pytest.param(-1, 1, id='negative_trivial_case'),
        (2, 4),
        (-2, 4),
    )
)
def test_square(input_x, expected):
    assert square(input_x) == expected
