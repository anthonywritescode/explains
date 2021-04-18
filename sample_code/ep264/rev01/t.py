import os.path


SOME_FILE = 'foo.txt'

# TOCTOU problem!
if os.path.exists(SOME_FILE):
    os.remove(SOME_FILE)


with open(SOME_FILE) as f:
    # RACE HERE
    f.write('new contents')
