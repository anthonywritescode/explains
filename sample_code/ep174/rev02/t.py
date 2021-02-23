import pytest


@pytest.mark.parametrize('a', (True, False))
@pytest.mark.parametrize(
    ('b', 'c', 'd'),
    (
        (True, True, True),
        (True, True, False),
        # ...
        (False, False, False),
    ),
)
def test_thing(a, b, c, d):
    ...
