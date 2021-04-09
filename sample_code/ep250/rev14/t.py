class C:
    def __init__(self, x):
        self.x = x


x = C(1)


match x:
    case int():
        print('matched an int')
    case float():
        print('matched a float')
    case C():
        print('matched a C')
    case _:
        print('matched nothing')
