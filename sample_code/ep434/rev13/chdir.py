import contextlib
import os


print(os.getcwd())

with contextlib.chdir(os.path.expanduser('~')):
    print(os.getcwd())

print(os.getcwd())
