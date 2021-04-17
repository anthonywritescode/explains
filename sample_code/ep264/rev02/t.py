import os.path
import tempfile


SOME_FILE = 'foo.txt'

fd, path = tempfile.mkstemp(dir=os.path.dirname(SOME_FILE))
with open(fd, 'w') as f:
    f.write('these are the new contents')

os.replace(path, SOME_FILE)
