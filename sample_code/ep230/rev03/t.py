import time


def f():
    return (1, ) * 1000000


t0 = time.monotonic_ns()

for _ in range(10):
    f()

t1 = time.monotonic_ns()


print(f'{(t1 - t0) / 100000000:.5f}')
