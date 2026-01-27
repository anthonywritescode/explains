from sentry.testutils.cases import TransactionTestCase
from sentry.models.environment import Environment


class Test1(TransactionTestCase):
    def test(self):
        Environment.get_or_create(
            self.project,
            'production',
        )

        assert len(Environment.objects.all()) == 1

    def test2(self):
        Environment.get_or_create(
            self.project,
            'production',
        )

        assert len(Environment.objects.all()) == 1
