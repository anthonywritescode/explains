
x = ['foo', 'baz']


match x:
    case ['baz', y]:
        print(f'got baz and {y=}')
    case ['foo', y]:
        print(f'got foo and {y=}')
