
x = 1  # global scope


def f():

    y = 2  # closure scoped
    z = 4

    def g():

        # z = 3  # local scope

        print(x, y, z)  # relative to here

        z = 3

    return g


g_func = f()

g_func()
