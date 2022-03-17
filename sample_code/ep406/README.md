# [the `split` command! (beginner - intermediate)](https://youtu.be/Ox95VqtRC28)

Today I show off the `split` command and some useful options for it!

## Interactive examples

### Bash

```bash
seq 1 100
seq 1 100 > f
nano f

man split
split -n 5 f
ls

nano xa*
rm x*

split -n r/5 f
nano xa*
rm xa*

split -n l/5 f
nano xa*

split -n l/5 f prefix_
ls

rm xa*
rm prefix*

split -x -n l/5 f prefix_
ls

split -x -n l/20 f prefix_
ls

rm prefix_*
split -n l/20 f prefix_
ls

find -name 'prefix*'
find -name 'prefix*' | sort
find -name 'prefix*' | sort | xargs cat
```
