from result import Ok, Err


def check(result):
    match result:
        case Ok(v):
            print(v)  # F821 undefined name 'v'
        case _:
            print("error")


check(Ok('test'))
check(Ok(1))
check(Err(0))
