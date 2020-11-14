try:
    with open('dne') as f:
        print(f.read(), end='')
except Exception:
    print('error happened!')
