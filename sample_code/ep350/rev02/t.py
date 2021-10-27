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
    signal.signal(signal.SIGALRM, alarm_handler)
    signal.alarm(s)
    yield


def main() -> int:
    with timeout(1):
        time.sleep(2)
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
