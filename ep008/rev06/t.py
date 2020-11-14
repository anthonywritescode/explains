import time


while True:
    try:
        print('zzz...')
        time.sleep(1)
    except BaseException:  # same as `except:`
        print('error happened!')
        raise
