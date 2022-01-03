# [job management: fg / bg / ^Z, & and more! (intermediate)](https://youtu.be/lkQOQAc65ZA)

Today I show backgrounding and foregrounding in the shell and kind of how it works from a signaling perspective!

## Interactive examples

### Bash

```bash
babi t.py
# Ctrl-z
python t.py
fg
# Ctrl-z
bg
jobs
fg

babi 1
# Ctrl-z
babi 2
# Ctrl-z
babi 3
# Ctrl-z
jobs
fg
# Ctrl-z
fg 2
# Ctrl-z
jobs

kill %3
jobs
fg 3

kill -9 %2
jobs
fg

python -c 'import time; time.sleep(10); print("hello hello")'
# Ctrl-z
fg

python -c 'import time; time.sleep(10); print("hello hello")' &
echo $!

python -c 'import time; time.sleep(10); print("hello hello")'
# Ctrl-z
bg
jobs

python -c 'import time; time.sleep(20); print("hello hello")'

ps -ef | grep python
kill -STOP <process_id>
jobs
bg
```
