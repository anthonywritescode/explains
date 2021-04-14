import sys

import pytest


def test_pass():
    assert 1 == 1


def test_failed():
    assert 1 == 2


@pytest.fixture
def fixture():
    yield
    assert False


def test_errored(fixture):
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
