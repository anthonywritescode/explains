

MISSING = object()


def func(dct):
    value = dct.get('k', MISSING)
    if value is MISSING:
        print('"k" was not supplied')
    else:
        print(f'this value was {value}')
