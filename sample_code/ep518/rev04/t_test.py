import t

import pytest


def test_square():
    assert t.square(5) == 25


def test_square_float():
    assert t.square(3.) == pytest.approx(10.)
