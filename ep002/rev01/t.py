def dec(func):
    return func


"""\
@dec
def f(x):
    print(f'hello {x}')
"""


def f(x):
    print(f'hello {x}')


f = dec(f)


f(1)
