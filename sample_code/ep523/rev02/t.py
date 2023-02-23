import dis


def f():
    if False:
        print('never runs')

    if __debug__:
        print('hi')

    print('hello hello')


f()
dis.dis(f)
