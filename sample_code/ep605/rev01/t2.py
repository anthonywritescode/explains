def _(x: str, **params: str) -> str:
    return x.format(**params)


language = input('what is your favorite language? ')

print(_('I love {language}'.format(language=language)))
