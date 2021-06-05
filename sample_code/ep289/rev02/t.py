x = [2, 5]

match x:
    case [1, y]:
        print(f'it started with 1 and had {y=}')
    case [2, y]:
        print(f'it started with 2 and had {y=}')
    case _:
        print('it was not matched')
