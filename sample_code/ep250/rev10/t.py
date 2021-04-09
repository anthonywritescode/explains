
x = ['foo', 'baz', 'foo']


match x:
    case ('baz', y):
        print(f'got baz and {y=}')
    case ('foo', y):
        print(f'got foo and {y=}')
    case _:
        print('nothing matched')
