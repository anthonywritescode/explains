# [the `comm` command! (intermediate)](https://youtu.be/Ic-8swynoHU)

Today I talk about the `comm` command and a few examples of how to use it!

## Interactive examples

### Bash

```bash
babi f1
babi f2
comm f1 f2

tail -n999 f*
man comm

comm -1 -2 f1 f2
comm -2 -3 f1 f2

comm -12 <(dpkg -l | awk '{print $2}' | sort) <(apt-cache rdepends python3 | awk '{print $1}' | sort)
dpkg -l | head -10
apt-cache rdepends python3 | head -10
```
