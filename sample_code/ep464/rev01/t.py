import math

import pytest


def f(x: float) -> float:
    return math.sqrt(x)


@pytest.mark.parametrize(
    ('input_val', 'cm'),
    (
        (-5, pytest.raises(ValueError)),
    ),
)
def test_f_errors(input_val, cm):
    with cm:
        f(input_val)
