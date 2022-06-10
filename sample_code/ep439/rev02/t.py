

def f(x: str | None) -> None:
    if x:
        reveal_type(x)
    else:
        reveal_type(x)
