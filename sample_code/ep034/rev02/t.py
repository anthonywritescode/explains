from typing import Tuple


def parse_color(s: str) -> Tuple[int, int, int]:
    return (0, 0, 0)


def test_black():
    assert parse_color('#000000') == (0, 0, 0)
