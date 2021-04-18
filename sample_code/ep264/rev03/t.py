import os.path
import tempfile


SOME_FILE = 'foo.txt'

fd, temp_path = tempfile.mkstemp(dir=os.path.dirname(SOME_FILE))
try:
    with open(fd) as f:
        f.write('these are the new contents\n')
    os.replace(temp_path, SOME_FILE)
except BaseException:
    os.remove(temp_path)
    raise
