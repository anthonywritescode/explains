import re

match = re.match('f', 'foo')

match match:
    case None:
        print('it did not match')
    case case:
        print(f'it matched {case}')
