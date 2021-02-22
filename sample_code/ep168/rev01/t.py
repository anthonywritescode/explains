import time


with open('foo', 'w') as f:
    time.sleep(.5)
    f.write('f')
    time.sleep(.5)
    f.write('0')
    time.sleep(.5)
    f.write('o\n')
    time.sleep(.5)
