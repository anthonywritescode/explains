import os
import signal
import time


def main():
    def handler(*a, **k):
        print('I got called')

    signal.signal(signal.SIGTERM, handler)

    os.kill(os.getpid(), signal.SIGTERM)
    time.sleep(.1)

    assert handler.call_count == 1, handler.call_count


if __name__ == '__main__':
    raise SystemExit(main())
