# [pgrep / pkill commands (beginner - intermediate)](https://youtu.be/KdSKTEUPPEk)

Today I show off the `pgrep` and `pkill` commands and how you can use them to find and signal processes!

## Interactive examples

### Bash

```bash
man pgrep

ps -ef | grep babi
pgrep babi

kill $(pgrep babi)
pkill babi
pkill -INT babi

ps -ef | grep babi | grep -v grep | grep -v avahi
ps -ef | grep babi | grep -v grep | grep -v avahi | awk '{print $2}'
ps -ef | grep babi | grep -v grep | grep -v avahi | awk '{print $2}' | xargs kill
```
