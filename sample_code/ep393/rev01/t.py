import signal
import time


def handler(*a, **k):
    print('signal ignored!')


signal.signal(signal.SIGTERM, handler)
time.sleep(5)
