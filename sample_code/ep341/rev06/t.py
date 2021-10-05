import signal
import time
from types import FrameType


class C:
    def __enter__(self):
        return self

    def __exit__(self, tp, exc, tb):
        print('world')


class SigTerm(SystemExit):
    pass


def term_cb(signal: int, frame: FrameType) -> None:
    raise SigTerm(1)


def main():
    signal.signal(signal.SIGTERM, term_cb)
    with C():
        time.sleep(100)
        print('hello')


if __name__ == '__main__':
    raise SystemExit(main())
