import unittest

import t

import pytest


@pytest.mark.parametrize(
    ('input_n', 'expected'),
    (
        (5, 25),
        (3., 9.),
    ),
)
def test_square(input_n, expected):
    print(f'{input_n=}')
    assert t.square(input_n) == expected


class TestSquare:
    def test_square(self):
        assert t.square(3) == 9


class TestLegacy(unittest.TestCase):
    def test(self):
        self.assertEqual(t.square(3), 9)
