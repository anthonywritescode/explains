try:
    with open('dne') as f:
        print(f.read(), end='')
except:  # noqa
    print('error happened!')


try:
    pass
except:  # noqa: E722
    print('error happened!')
