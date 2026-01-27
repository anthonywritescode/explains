import os
import sys


with open(sys.argv[1]) as f:
    testids = [
        line for line in f.read().splitlines()
        if not line.startswith('#')
    ]

cmd = ('pytest', '-q', *sys.argv[2:], *testids)
os.execvp(cmd[0], cmd)
