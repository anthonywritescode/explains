# [don't use os.system! (beginner - intermediate)](https://youtu.be/oQxTSDh-ECk)

Today I talk about why you shouldn't use `os.system` and instead use subprocess in python!

## Interactive examples

### Python

```python
import os
os.system('/bin/sleep 100')

open('`touch pwnd`', 'w').close()
os.listdir()

with open('foo', 'w') as f:
    f.write('hello world\n')

files = os.listdir()
files

f'head -10 {" ".join(files)}'
os.system(f'head -10 {" ".join(files)}')
os.listdir()
os.remove('pwnd')

import subprocess
subprocess.call(('head', '-10', *files))
os.listdir()

subprocess.call(f'head -10 {" ".join(files)}', shell=True)
os.listdir()

import shlex
shlexed = [shlex.quote(f) for f in files]
shlexed
cmd = f'head -10 {" ".join(shlexed)}'
cmd
os.system(cmd)

stdout = subprocess.check_output(('head', '-10', *files))
print(stdout.decode())
stdout
```

### Bash

```bash
ps -ef | grep python3
watch pstree -halp <process_id>
```
