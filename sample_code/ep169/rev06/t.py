def f():
    class notlocal:
        x = ()

    def modify_x():
        notlocal.x = (2,)

    modify_x()

    return notlocal.x


print(f())
