# [python: os.exec* vs subprocess (intermediate)](https://youtu.be/xTiPODNalrU)

Today I talk about the difference between the os.exec* functions (execvp, execvpe, etc.) and the subprocess functions and why I use a particular one and why exec is HORRIBLY BROKEN on windows

## Interactive examples

### Python

Session 1:

```python
import subprocess
subprocess.call(('sleep', '10'))

import os
help(os.execvp)
cmd = ['sleep', '10']
os.execvp(cmd[0], cmd)
```

Session 2:

```python
import os
cmd = ['bash', '-c', 'exit 1']
os.execvp(cmd[0], cmd)

```

### Bash

```bash
aws s3 --help
aws s3 help
babi awshelp.py

ps -ef | grep python
watch pstree -halp <process_id>
```

### Windows CMD

```batch
echo %ERRORLEVEL%
```
