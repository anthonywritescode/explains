# [more powerful than control-C (beginner - intermediate)](https://youtu.be/_f8xgOMGO-g)

Today I share another tip I wish I knew earlier -- a more powerful keyboard to terminate commands than ^C!

## Interactive examples

### Bash

```bash
python t.py
# Ctrl-c
# Ctrl-z
bg
fg
# Ctrl-z
kill %1
ps -ef | grep python

python t.py
# Ctrl-\
ls core
```
