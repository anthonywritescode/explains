import subprocess

print('before readline')
subprocess.check_call(('env',))

import readline
import os

os.environ['COLUMNS'] = os.environ['LINES'] = ''
del os.environ['COLUMNS'], os.environ['LINES']

print('after readline')
subprocess.check_call(('env',))
