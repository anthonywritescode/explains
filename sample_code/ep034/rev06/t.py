from typing import Tuple

import pytest


def parse_color(s: str) -> Tuple[int, int, int]:
    if len(s) == 7:
        return int(s[1:3], 16), int(s[3:5], 16), int(s[5:7], 16)
    elif len(s) == 4:
        return int(s[1] * 2, 16), int(s[2] * 2, 16), int(s[3] * 2, 16)
    else:
        raise ValueError(f'unknown color format: {s}')


@pytest.mark.parametrize(
    ('input_s', 'expected'),
    (
        ('#000000', (0, 0, 0)),
        ('#ffffff', (0xff, 0xff, 0xff)),
        ('#000', (0, 0, 0)),
    ),
)
def test_parse_color(input_s, expected):
    assert parse_color(input_s) == expected
