import pytest


def square(n: int) -> int:
    return n * n


@pytest.mark.parametrize(
    ('input_x', 'expected', 'error'),
    (
        (1, 1, False),
        pytest.param(-1, 1, False, id='negative_trivial_case'),
        (2, 4, False),
        (-2, 4, False),
        ('a', None, True),
        ([], None, True),
    )
)
def test_square(input_x, expected, error):
    if error:
        with pytest.raises(TypeError):
            square(input_x)
    else:
        assert square(input_x) == expected
