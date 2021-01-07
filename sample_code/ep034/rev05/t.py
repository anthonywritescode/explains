from typing import Tuple


def parse_color(s: str) -> Tuple[int, int, int]:
    if len(s) == 7:
        return int(s[1:3], 16), int(s[3:5], 16), int(s[5:7], 16)
    elif len(s) == 4:
        return int(s[1] * 2, 16), int(s[2] * 2, 16), int(s[3] * 2, 16)
    else:
        raise ValueError(f'unknown color format: {s}')


def test_black():
    assert parse_color('#000000') == (0, 0, 0)


def test_white():
    assert parse_color('#ffffff') == (0xff, 0xff, 0xff)


# #999 -> #909090 or #999999

def test_black_short():
    assert parse_color('#000') == (0, 0, 0)
