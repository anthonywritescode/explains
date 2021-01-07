

while True:
    try:
        print('zzz')
        raise KeyboardInterrupt()
    except BaseException:
        print('got BaseException')
        raise
    except:
        print('some other error happened!')
        raise
