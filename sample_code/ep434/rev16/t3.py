import sys

try:
    raise AssertionError('hi')
except Exception:
    tp, value, tb = sys.exc_info()
    print(repr(tp), repr(value), repr(tb))

    print(repr(type(value)), repr(value), repr(value.__traceback__))
