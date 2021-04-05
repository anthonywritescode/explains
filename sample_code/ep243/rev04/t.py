import enum

_Status = enum.Enum('_Status', 'MISSING')
_MISSING = _Status.MISSING


def func(dct):
    value = dct.get('k', _MISSING)
    if value is _MISSING:
        print('"k" was not supplied')
    else:
        print(f'this value was {value!r}')
