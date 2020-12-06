try:
    with open('dne') as f:
        print(f.read(), end='')
except:
    print('error happened!')
