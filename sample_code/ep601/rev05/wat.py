from sentry.testutils.cases import TransactionTestCase
from sentry.models.environment import Environment


class Test1(TransactionTestCase):
    def test(self):
        env = Environment.get_or_create(
            self.project,
            'production',
        )

        assert env.id == 1

    def test2(self):
        env = Environment.get_or_create(
            self.project,
            'production',
        )

        assert env.id == 1
