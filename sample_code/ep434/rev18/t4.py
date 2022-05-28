import contextlib
import os
import unittest


class TestThing(unittest.TestCase):
    def setUp(self):
        self.enterContext(contextlib.chdir(os.path.expanduser('~')))

    def test_thing(self):
        print('hi from test')
        print(f'cwd: {os.getcwd()}')
