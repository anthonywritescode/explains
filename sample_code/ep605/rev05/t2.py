from typing import LiteralString

LANG = 'es_US'

TRANSLATIONS = {
    'I love {language}': {
        'en_US': 'I love {language}',
        'es_US': 'a mi me gusta {language}',
    }
}


def _(x: LiteralString, **params: str) -> str:
    format_str = TRANSLATIONS.get(x, {}).get(LANG, x)
    return format_str.format(**params)


language = input('what is your favorite language? ')

print(_('I love {language}', language=language))
