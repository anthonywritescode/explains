import os
import signal
import time
from unittest import mock


def main():
    handler = mock.Mock()

    signal.signal(signal.SIGTERM, handler)

    os.kill(os.getpid(), signal.SIGTERM)
    time.sleep(.1)

    assert handler.call_count == 1


if __name__ == '__main__':
    raise SystemExit(main())
