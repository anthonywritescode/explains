import pytest


class C:
    def f(self):
        return 1

    def g(self):
        return 2


@pytest.fixture
def c_instance():
    return C()


def test_f(c_instance):
    assert c_instance.f() == 1


def test_g(c_instance):
    assert c_instance.g() == 2
