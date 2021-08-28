# [the `uniq` command (+ some `sort`) (beginner - intermediate)](https://youtu.be/FMdWB3m3lQ0)

Today I talk about the `uniq` command and also a little bit about `sort`!

## Interactive examples

### Bash

```bash
history | grep uniq
history | grep 'sort -u'

uniq t
uniq t -c
uniq t -c | sort -r
uniq t -c | sort
uniq t -c | sort -n

uniq t -c
uniq t
sort t | uniq
sort -u t
```
