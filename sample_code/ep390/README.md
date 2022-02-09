# [how an exit(n) bug introduced 100s of lint errors (intermediate)](https://youtu.be/RVSw1BGNmq8)

Today I talk about a funny bug where a `exit(...)` but allowed hundreds of linting errors to enter the primary branch

## Interactive examples

### Bash

```bash
python t.py
echo $?

python -c 'import time; time.sleep(10)'
echo $?

kill -l

python -c 'import time; time.sleep(10)'
ps -ef | grep sleep
kill -TERM <process_id>
echo $?
```
