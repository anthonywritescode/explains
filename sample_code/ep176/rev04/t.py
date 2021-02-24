from typing import Tuple


def parse_version(s: str) -> Tuple[int, int]:
    return tuple(int(part) for part in s.split('.'))


import pytest


@pytest.mark.parametrize(
    ('input_s', 'expected'),
    (
        ('2.7', (2, 7)),
        ('3.6', (3, 6)),
        ('3.10', (3, 10)),
    ),
)
def test_parse_version(input_s, expected):
    assert parse_version(input_s) == expected


def test_parse_version_not_a_number():
    try:
        parse_version('3.6')
    except ValueError as e:
        assert e
    else:
        raise AssertionError('expected to raise ValueError')


def test_parse_version_failure():
    ...
