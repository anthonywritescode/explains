import itertools

import pytest


CONSTANT_WORD = 'food'
_PERMUTATIONS = frozenset(
    ''.join(word)
    for word in itertools.permutations(CONSTANT_WORD)
)


def is_anagram_of_constant_word(word2: str) -> bool:
    return word2 in _PERMUTATIONS


def is_anagram(word1: str, word2: str) -> bool:
    for permutation1 in itertools.permutations(word1):
        for permutation2 in itertools.permutations(word2):
            if permutation1 == permutation2:
                return True

    return False


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
