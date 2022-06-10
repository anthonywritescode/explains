

def f(x: str | None) -> None:
    if x is None:
        reveal_type(x)
        print('got None')
    else:
        reveal_type(x)
        print('got string ' + x)
