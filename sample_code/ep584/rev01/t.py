from unittest import TestCase

g = True


class TestCaseTest(TestCase):
    @classmethod
    def tearDownClass(cls):
        print('class teardown!')

    def test(self):
        global g
        print('test!')
        if g:
            print('flaky fail!')
            g = False
            raise AssertionError('#')
