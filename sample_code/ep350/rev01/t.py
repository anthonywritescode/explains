import contextlib
import signal
import time
from typing import Generator


@contextlib.contextmanager
def timeout(s: int) -> Generator[None, None, None]:
    signal.alarm(s)
    yield


def main() -> int:
    with timeout(1):
        time.sleep(2)
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
