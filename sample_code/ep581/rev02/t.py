import warnings


@warnings.deprecated('use foo instead')
def bar(*a, **k):
    return foo(*a, **k)


def foo(x):
    print(f'got {x=}')


bar(1)
