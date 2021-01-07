import string
from typing import NamedTuple


class Point(NamedTuple):
    x: int
    y: int


thing = 'world'
point = Point(10, 15)
temperature = 21.567


# concatenation-based string formatting
print(
    'hello ' + repr(thing) + ' ' +
    'I am at ' + str(point.x) + ', ' + str(point.y) + ' '
    'and my temperature is ' + format(temperature, '.1f')
)


# string.Template
template = string.Template(
    'hello ${thing} '
    'I am at ${x}, ${y} '
    'and my temperature is ${temp}',
)

print(
    template.substitute(
        thing=repr(thing),
        x=point.x, y=point.y,
        temp=format(temperature, '.1f'),
    )
)


# %-format
print(
    'hello %(thing)r '
    'I am at %(x)s, %(y)s '
    'and my temperature is %(temp).1f' % {
        'thing': thing, 'x': point.x, 'y': point.y, 'temp': temperature,
    }
)

print(
    'hello %r '
    'I am at %s, %s '
    'and my temperature is %.1f' % (thing, point.x, point.y, temperature),
)


# .format
print(
    'hello {thing!r} '
    'I am at {x}, {y} '
    'and my temperature is {temp:.1f}'.format(
        thing=thing, x=point.x, y=point.y, temp=temperature,
    )
)

print(
    'hello {!r} '
    'I am at {}, {} '
    'and my temperature is {:.1f}'.format(
        thing, point.x, point.y, temperature,
    ),
)

print(
    'hello {thing!r} '
    'I am at {point.x}, {point.y} '
    'and my temperature is {temp:.1f}'.format(
        thing=thing, point=point, temp=temperature,
    )
)


# f-strings
print(
    f'hello {thing!r} '
    f'I am at {point.x}, {point.y} '
    f'and my temperature is {temperature:.1f}'
)

print(
    f'hello {thing!r} '
    f'I am at {point.x}, {point.y=} '
    f'and my temperature is {temperature:.1f}'
)
