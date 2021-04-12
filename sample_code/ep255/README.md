# [speed up git in big repos with this trick (beginner)](https://youtu.be/ppILYNc10DQ)

Today I show a little tip for speeding up `git` operations in large repositories by enabling a feature flag!  this made `git status` in a work repo go from 2+ seconds to 450ms!

## Interactive examples

### Bash

```bash
git clone git@github.com:torvalds/linux --depth 1
# git clone https://github.com/torvalds/linux --depth 1
cd linux

time git status
time git status

git config feature.manyFiles 1

time git status
time git status

nano .git/config
man git config
```
