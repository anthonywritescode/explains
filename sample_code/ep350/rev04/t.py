import contextlib
import signal
import time
from types import FrameType
from typing import Generator


class TimeoutError(Exception):
    pass


def alarm_handler(signum: int, frame: FrameType) -> None:
    print(signum, frame)
    raise TimeoutError()


@contextlib.contextmanager
def timeout(s: int) -> Generator[None, None, None]:
    orig = signal.signal(signal.SIGALRM, alarm_handler)
    signal.alarm(s)
    try:
        yield
    finally:
        signal.alarm(0)
        signal.signal(signal.SIGALRM, orig)


def main() -> int:
    with timeout(1):
        pass

    time.sleep(2)

    return 0


if __name__ == '__main__':
    raise SystemExit(main())
