import subprocess

print('before readline')
subprocess.check_call(('env',))

import readline
print('after readline')
subprocess.check_call(('env',))
