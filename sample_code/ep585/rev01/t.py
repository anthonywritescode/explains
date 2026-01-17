def __getattr__(x: str) -> object:
    print(f'looking for {x}')
    return x * 2
