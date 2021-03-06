import os
import time
import tempfile


with tempfile.NamedTemporaryFile(dir='.') as tmpfile:
    ...


with open('foo.tmp', 'w') as f:
    time.sleep(.5)
    f.write('f')
    time.sleep(.5)
    f.write('0')
    f.flush()
    time.sleep(.5)
    f.write('o\n')
    time.sleep(.5)

os.replace('foo.tmp', 'foo')
