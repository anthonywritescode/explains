from typing import NamedTuple


class Point(NamedTuple):
    x: int
    y: int


thing = 'world'
point = Point(10, 15)
temperature = 21.567


# concatenation-based string formatting
print(
    'hello ' + thing + ' ' +
    'I am at ' + str(point.x) + ', ' + str(point.y) + ' '
    'and my temperature is ' + format(temperature, '.1f')
)
