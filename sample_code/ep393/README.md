# [the `timeout` command (beginner - intermediate)](https://youtu.be/QRywzsBftfc)

today I walk through the `timeout` command and the useful options for it!  I recently showed this off in another video and felt it needed more explanation :D

## Interactive examples

### Bash

```bash
man timeout

timeout 1 sleep 5
echo $?

timeout 1 python t.py
timeout --kill-after=2 1 python t.py
echo $?

timeout --signal=INT 1 python t.py
timeout --signal=INT --kill-after=5 180 python t.py
```
