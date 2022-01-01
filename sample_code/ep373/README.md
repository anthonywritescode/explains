# [git commit as someone else? (intermediate)](https://youtu.be/bQ2OiciywyA)

Today I show how to use temporary git configuration on the command line to commit as someone else

## Interactive examples

### Bash

```bash
nano ~/.gitconfig

git init wat
cd !$
nano .git/config

git commit --allow-empty -m 'empty initial commit'
git -c user.name='Linus Torvalds' -c user.email='torvalds@linux-foundation.org' commit -m 'I AM LINUS' --allow-empty
git log

nano .git/hooks/post-checkout
chmod +x !$

git checkout HEAD -b foo
git checkout HEAD -b bar --no-verify
git -c core.hooksPath=/dev/null checkout HEAD -b bar

# git clone https://github.com/pre-commit/pre-commit
# cd pre-commit
git grep "git.*'-c'"
```
