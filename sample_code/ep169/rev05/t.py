def f():
    x = ()

    def modify_x():
        nonlocal x
        x = (2,)

    modify_x()

    return x


print(f())
