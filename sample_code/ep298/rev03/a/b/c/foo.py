from .bar import x
from . import bar
from .. import b
from ... import a


print(f'got from bar: {x=}')
print(f'got from bar: {bar=}')
print(f'got {b=}')
print(f'got {a=}')
