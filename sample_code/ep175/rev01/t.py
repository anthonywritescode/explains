import time


while True:
    try:
        print('zzz', flush=True)
        time.sleep(1)
    except:
        print('ignoring exception...')
