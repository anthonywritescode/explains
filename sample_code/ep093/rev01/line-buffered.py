import sys
import time


for i in range(10):
    print(f'log line {i}', file=sys.stderr)
    time.sleep(.25)
