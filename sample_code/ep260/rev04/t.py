import sys

import pytest


def test_pass():
    assert 1 == 1


@pytest.mark.skip(reason='this is broken')
def test_skipped():
    pass


@pytest.mark.skipif(sys.platform == 'linux', reason='windows behaviour')
def test_skipped_conditionally():
    pass


@pytest.mark.xfail
def test_expected_to_fail():
    assert False


@pytest.mark.xfail
def test_expected_to_fail_but_passing():
    pass
