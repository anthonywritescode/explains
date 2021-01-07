import subprocess

# convention:
# def f(*args, **kwargs):


def f(a, /, b, c=2, *d, e, f=2, **g):
    print(f'a is {a}')
    print(f'b is {b}')
    print(f'c is {c}')
    print(f'd is {d}')
    print(f'e is {e}')
    print(f'f is {f}')
    print(f'g is {g}')


subprocess.check_call(('echo', 'hi'))


def _check_call(*cmd, **kwargs):
    subprocess.check_call(cmd, **kwargs)
