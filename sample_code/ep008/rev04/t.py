import time


while True:
    try:
        print('zzz...')
        time.sleep(1)
    except:
        print('error happened!')


# under Linux/Unix, you can use Ctrl-\ for SIGQUIT
# under Windows, you can use Ctrl-Pause|Break for SIGBREAK
