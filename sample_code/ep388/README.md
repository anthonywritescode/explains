# [time vs. /bin/time (beginner - intermediate)](https://youtu.be/hJ5LT4AGf3Y)

Today I talk about the differences between the shell builtin and the command `time` and some cool uses for both of them!

## Interactive examples

### Bash

```bash
type time

which time
which -a time

ls -ald /usr/bin
ls -ald /bin

time sleep 1
time echo hi | sleep 1

/bin/time sleep 1
/bin/time echo hi | sleep 1

(time echo hi) | sleep 1

/bin/time -v python -c 'print("hello world")'
/bin/time --format %M python -c '[9] * 99999999'

time echo hi
\time echo hi
t\ime echo hi

type nano
nano
\nano
```
