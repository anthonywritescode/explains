import unittest

import pytest


def f(x, y):
    if x != y:
        raise ValueError(x, y)


class TestThing(unittest.TestCase):
    def test_f(self):
        x = 1
        y = 2
        with pytest.raises(TypeError):
            f(x, y)
