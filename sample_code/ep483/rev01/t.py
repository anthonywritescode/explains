class C:
    def __del__(self):
        raise AssertionError('oh no!')


def test_foo():
    C()
