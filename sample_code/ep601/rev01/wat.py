from sentry.testutils.cases import TestCase
from sentry.models.environment import Environment


class Test1(TestCase):
    def test(self):
        Environment.get_or_create(self.project, 'production')
        assert len(Environment.objects.all()) == 1


class Test2(TestCase):
    def test(self):
        assert len(Environment.objects.all()) == 0
