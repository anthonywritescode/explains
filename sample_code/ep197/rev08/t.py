

x = 1  # global scope


def f():

    y = 2  # closure scoped
    z = 4

    def g():

        z = 3  # local scope

        for z in range(5):
            print(f'{z=}')

        print(z)

        print(x, y, z)  # relative to here

    g()


f()
