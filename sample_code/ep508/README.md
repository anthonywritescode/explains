# [don't use cat! (intermediate)](https://youtu.be/vWMiBVkdJjA)

Today I talk about the `cat` command -- and that it's almost always unnecessary!

## Interactive examples

### Bash

```bash
echo foo > f1
echo bar > f2

cat f1 f2
cat f1

babi f1
cat f1
cat f1 | grep '^foo'

grep '^foo' f1
grep '^foo' < f1
```
