from __future__ import annotations

import itertools

import pytest

# 1. read the question
# 2. ask any clarifying questions
# 3. state any assertions
# 4. speak through a general thought process
#    - what needs to be done
#    - what the performance will be
# 5. TDD: write up some test cases
#    - use whatever testing library for your language
#    - come up with edge cases
#    - don't worry about finding all of them up front
# 6. actually implement the thing
#    1. (!!!) make it work at all
#    2. (!) make it performant
#    3. make the code readable
# 7. talk about algorithmic performance


def cbh(hours: list[tuple[int, int]]) -> list[tuple[int, int]]:
    if len(hours) <= 1:
        return list(hours)

    ret = [hours[0]]

    for start, end in itertools.islice(hours, 1, None):
        if ret[-1][1] == start:
            ret[-1] = (ret[-1][0], end)
        else:
            ret.append((start, end))

    return ret


@pytest.mark.parametrize(
    ('input_hours', 'expected'),
    (
        ([], []),
        (
            [(1, 2)],
            [(1, 2)]
        ),
        (
            [(1, 2), (2, 3), (5, 6)],
            [(1, 3), (5, 6)],
        ),
        (
            [(1, 3), (5, 6)],
            [(1, 3), (5, 6)],
        ),
        (
            [(1, 2), (2, 3), (3, 4)],
            [(1, 4)],
        ),
    ),
)
def test_cbh(input_hours, expected):
    assert cbh(input_hours) == expected


def test_does_not_mutate_input():
    lst = [(1, 2), (2, 3), (5, 6)]
    cbh(lst)
    assert lst == [(1, 2), (2, 3), (5, 6)]


if __name__ == '__main__':
    raise SystemExit(pytest.main([__file__]))
