
x = {'foo': 'bar', 'baz': 'womp'}


match x:
    case {'bar': bar}:
        print(f'the dictionary had a key bar with value {bar}')
    case {'foo': foo}:
        print(f'the dictionary had a key foo with value {foo}')
    case _:
        print('nothing matched')
