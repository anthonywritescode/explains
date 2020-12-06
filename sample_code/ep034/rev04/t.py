from typing import Tuple


def parse_color(s: str) -> Tuple[int, int, int]:
    return int(s[1:3], 16), int(s[3:5], 16), int(s[5:7], 16)


def test_black():
    assert parse_color('#000000') == (0, 0, 0)


def test_white():
    assert parse_color('#ffffff') == (0xff, 0xff, 0xff)


# #999 -> #909090 or #999999

def test_black_short():
    assert parse_color('#000') == (0, 0, 0)
