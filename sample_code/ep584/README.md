# [debugging flaky cascading failure after upgrading pytest!](https://youtu.be/zyZXdvJgGPM)

another deep dive debugging session!  I utilize a dirty bisect to figure out what introduced the behaviour.  from there test pollution helped me find a reproduction and then I isolated what was interfering and utilized a new technique to find _why_!

## Setup commands

```bash
git clone git@github.com:pytest-dev/pytest
git clone git@github.com:getsentry/sentry
```

## Interactive examples

### Python

```python
import sys
import pytest


@pytest.fixture(autouse=True, scope='session')
def settrace():
    with open(f'trace.{os.getpid()}', 'a+') as f:
        def tracefunc(frame, event, arg):
            if (
                event == 'call' and
                '/new_migrations/monkey/' not in frame.f_code.co_filename and
                any(
                    s in frame.f_code.co_filename
                    for s in (
                        '/src/sentry/testutils/', '/tests/sentry/',
                        '/django/test/', '/pytest_django/',
                )
            ):
                f.write(f'{frame.f_code.co_filename}:{frame.f_code.co_name}\n')

        orig = sys.settrace(tracefunc)
        yield
        sys.settrace(orig)
```

### Bash

Session 1:

```bash
cd pytest/
git log --oneline --first-parent 8.1.0..8.2.0
git log --oneline --first-parent 8.1.0..8.2.0 -- src
```

Session 2:

```bash
cd sentry/
pytest --setup-plan tests/sentry/utils/test_math.py | less

diff -u planbefore planafter | less
jq . last-failed-list
diff -u trace.old trace.new | less

virtualenv venv
./venv/bin/pip install pytest pytest-rerunfailures
./venv/bin/pytest --reruns=2 -s t.py
```
