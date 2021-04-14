

def gen():
    yield 1
    yield 2
    yield 3


def gen2():
    yield 9000
    yield from gen()
    yield 9001


for thing in gen2():
    print(f'got thing: {thing}')
