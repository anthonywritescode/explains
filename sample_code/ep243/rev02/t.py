

_MISSING = object()


def func(dct):
    value = dct.get('k', _MISSING)
    if value is _MISSING:
        print('"k" was not supplied')
    else:
        print(f'this value was {value!r}')
