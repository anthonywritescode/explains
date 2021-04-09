class C:
    __match_args__ = ('x', 'y')

    def __init__(self, x, y):
        self.x = x
        self.y = y


x = C(1, 2)


match x:
    case int():
        print('matched an int')
    case float():
        print('matched a float')
    case C(1, 1):
        print('matched a C(1, 1)')
    case C(1, 2):
        print('matched a C(1, 2)')
    case C(x=2):
        print('matched a C w/ x = 2')
    case C(x=1):
        print('matched a C w/ x = 1')
    case _:
        print('matched nothing')
