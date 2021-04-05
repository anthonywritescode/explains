

def func(dct):
    value = dct.get('k')
    if value is None:
        print('"k" was not supplied')
    else:
        print(f'this value was {value!r}')
