from collections import Counter

import pytest


# write a function is_anagram(w1, w2)
#
# two words are anagrams if you can rearrange the letters and they are the
# same


def is_anagram_via_sorting(w1: str, w2: str) -> bool:
    return sorted(w1) == sorted(w2)


def is_anagram(w1: str, w2: str) -> bool:
    return Counter(w1) == Counter(w2)


@pytest.mark.parametrize(
    ('w1', 'w2', 'expected'),
    (
        ('', '', True),
        ('', 'a', False),
        ('a', 'b', False),
        ('bleat', 'table', True),
        ('foo', 'of', False),
        ('foo', 'ffo', False),
    )
)
def test_is_anagram(w1, w2, expected):
    assert is_anagram(w1, w2) is expected
