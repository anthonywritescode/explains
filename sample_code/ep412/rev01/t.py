from typing import Mapping


def f(dct: Mapping[str, str]) -> None:
    dct['foo'] = 'bar'


dct = {'bar': 'baz'}
f(dct)
print(dct)
