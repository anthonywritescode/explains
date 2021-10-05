import time


class C:
    def __enter__(self):
        return self

    def __exit__(self, tp, exc, tb):
        print('world')


with C():
    time.sleep(100)
    print('hello')
