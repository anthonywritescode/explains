import sys

try:
    raise AssertionError('hi')
except Exception:
    value = sys.exception()
    print(repr(type(value)), repr(value), repr(value.__traceback__))
