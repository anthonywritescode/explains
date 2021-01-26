import re


pattern = re.compile('foo')


match = pattern.match('food')
reveal_type(match)
