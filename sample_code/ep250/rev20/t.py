class C:
    __match_args__ = ('x', 'y')

    def __init__(self, x, y):
        self.x = x
        self.y = y


x = 15


match x ** 3:
    case int() as matched_val if x > 10:
        print(f'matched an int {matched_val}')
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
