import dis


def f():
    if __debug__:
        print('hi')
    print('hello hello')


f()
dis.dis(f)
