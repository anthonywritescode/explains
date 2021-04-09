class C:
    def __init__(self, x):
        self.x = x


x = C(1)


match x:
    case int():
        print('matched an int')
    case float():
        print('matched a float')
    case C(x=2):
        print('matched a C w/ x = 2')
    case C(x=1):
        print('matched a C w/ x = 1')
    case _:
        print('matched nothing')
