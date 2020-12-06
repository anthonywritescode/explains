

def gen():
    yield 1
    print('hello')
    yield 2
    print('world')
    yield 3


gen()

for _ in gen():
    pass

tuple(gen())
list(gen())
