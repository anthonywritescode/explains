import tempfile

import pytest


class C:
    def f(self):
        return 1

    def g(self):
        return 2


@pytest.fixture
def temporary_dir():
    with tempfile.TemporaryDirectory() as tmpdir:
        yield tmpdir


@pytest.fixture
def c_instance(temporary_dir):
    return C()


@pytest.fixture(autouse=True, scope='session')
def setup_teardown():
    print('setup')
    yield
    print('teardown')


@pytest.fixture(name='fix')
def lkajsdlifjalksdjflkasdf():
    return 5


@pytest.fixture(params=(1, 2, 3, 4))
def an_int(request):
    yield request.param + 2


def test_an_int(an_int):
    print(f'got {an_int=}')


def test_with_setup_teardown(fix):
    print(f'in test {fix=}')


def test_f(c_instance):
    assert c_instance.f() == 1


@pytest.mark.usefixtures('setup_teardown')
def test_g(c_instance):
    assert c_instance.g() == 2


class TestMyThing:
    @pytest.fixture
    def fix(self):
        yield 10

    def test_1(self, fix):
        print(f'got {fix=}')
