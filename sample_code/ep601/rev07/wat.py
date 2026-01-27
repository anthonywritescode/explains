from sentry.testutils.cases import TestCase, TransactionTestCase
from sentry.models.environment import Environment


class Test1(TransactionTestCase):
    reset_sequences = True

    def test(self):
        env = Environment.get_or_create(
            self.project,
            'production',
        )

        assert env.id == 1


class Test2(TestCase):
    def test2(self):
        env = Environment.get_or_create(
            self.project,
            'production',
        )

        assert env.id == 1
