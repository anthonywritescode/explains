import pytest


@pytest.mark.parametrize(
    ('a', 'b', 'c', 'd'),
    (
        (True, True, True, True),
        (False, True, True, True),
        # ...
        (False, False, False, False),
    ),
)
def test_thing(a, b, c, d):
    ...
