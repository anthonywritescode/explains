# [oops I typed `git git ...` again (beginner - intermediate)](https://youtu.be/BkUW2NgfZao)

Today I show a neat little alias that kevinsjoberg in my chat showed off that makes a common `git` typo go away!

## Interactive examples

### Bash

```bash
git init foo
cd !$
cd foo
ls

git git commit -m 'foo' --allow-empty

git config --global alias.git  '!git'
git git commit -m 'foo' --allow-empty

git git git git git git git git status
```
