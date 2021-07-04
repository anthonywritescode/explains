

def foo(x: int) -> float:
    reveal_type(x)
    y = x + 5.5
    reveal_type(y)
    z = x ** 10
    reveal_locals()
    return y + z


q = foo(5)
