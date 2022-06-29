# [configuring git from environment vars (intermediate)](https://youtu.be/RVZeTpVpwS4)

Someone showed me a neat feature in newer versions of git so I figured I'd show you in a video!

## Interactive examples

### Bash

```bash
git --version

# git clone https://github.com/git/git
git clone git@github.com:git/git --depth=1
cd git
git remote -v

make prefix=$PWD/prefix -j6 install

git log -G GIT_CONFIG_KEY
git log -G GIT_CONFIG_KEY -- '*.c'
git show <commit_hash>
git describe --contains <commit_hash>

ls prefix/bin/
export PATH=$PWD/prefix/bin:$PATH
git --version

git init wat
cd !$

export GIT_CONFIG_KEY_0=user.name
export GIT_CONFIG_VALUE_0='Jeffy Jeff'
export GIT_CONFIG_COUNT=1

# export GIT_CONFIG_KEY_1=user.email
# export GIT_CONFIG_VALUE_1='jeffy.jeff@example.com'
# export GIT_CONFIG_COUNT=2

git commit --allow-empty -m 'initial empty commit'
git show

nano /etc/environment
```
