import time


def f():
    return (1, ) * 1000000


t0 = time.time()

for _ in range(10):
    f()

t1 = time.time()


print(f'{t1 - t0:.5f}')
