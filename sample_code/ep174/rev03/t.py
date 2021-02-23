import pytest


@pytest.mark.parametrize('a', (True, False))
@pytest.mark.parametrize('b', (True, False))
@pytest.mark.parametrize('c', (True, False))
@pytest.mark.parametrize('d', (True, False))
def test_thing(a, b, c, d):
    ...
