# -*- coding: dict-unpacking-at-home -*-

dct = {'greeting': 'hello', 'thing': 'world'}

{greeting, thing} = dct
print(greeting, greeting, thing)

dct2 = {'greeting': 'hello', 'other': [2, 3, 4]}
{greeting, 'other': [first, *rest]} = dct2
print(greeting, first, rest)
