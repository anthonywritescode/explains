

def gen():
    yield 1
    yield 2
    yield 3


for thing in gen():
    print(f'got thing: {thing}')
