import concurrent.futures
from sentry.testutils.cases import TestCase
from sentry.models.environment import Environment


class Test1(TestCase):
    def test(self):
        with concurrent.futures.ThreadPoolExecutor() as exe:
            fut = exe.submit(
                Environment.get_or_create,
                self.project,
                'production',
            )
            fut.result()

        assert len(Environment.objects.all()) == 1


class Test2(TestCase):
    def test(self):
        assert len(Environment.objects.all()) == 0
