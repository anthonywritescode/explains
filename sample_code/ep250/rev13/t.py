class C:
    pass


x = C()


match x:
    case int():
        print('matched an int')
    case float():
        print('matched a float')
    case C():
        print('matched a C')
    case _:
        print('matched nothing')
