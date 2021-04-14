import pytest


def test_pass():
    assert 1 == 1


def test_failed():
    assert 1 == 2


@pytest.fixture
def fixture():
    assert False


def test_errored(fixture):
    assert 1 == 1
