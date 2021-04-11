import collections

import pytest


def is_anagram(word1: str, word2: str) -> bool:
    return collections.Counter(word1) == collections.Counter(word2)


@pytest.mark.parametrize(
    ('word1', 'word2'),
    (
        ('', ''),
        ('a', 'a'),
        ('of', 'fo'),
        ('oof', 'foo'),
    ),
)
def test_matches(word1, word2):
    assert is_anagram(word1, word2) is True


@pytest.mark.parametrize(
    ('word1', 'word2'),
    (
        ('a', 'b'),
        ('of', 'off'),
        ('oof', 'ffo'),
    ),
)
def test_notmatches(word1, word2):
    assert is_anagram(word1, word2) is False
