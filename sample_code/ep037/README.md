# [git: useful trick for pushing branches (beginner - intermediate)](https://youtu.be/bItxrNqJ5UQ)

Today I share a useful trick that I get asked about a lot on stream when pushing branches!

## Setup commands

```bash
git clone git@github.com:<your_github_username>/pyupgrade
```

## Interactive examples

### Bash

```bash
cd pyupgrade
git checkout origin/master -b i-am-fixing-the-thing
git commit -m 'fix the thing' --allow-empty

# git push
git push origin i-am-fixing-the-thin
# git push origin i-am-fixing-the-thing
git push origin HEAD

cd ..
git clone git@github.com:pycqa/pycodestyle
cd pycodestyle

# git github-fork
git remote add <your_github_username> git@github.com:<your_github_username>/pycodestyle
git remote -v

git checkout origin/master -b i-am-fixing-the-thing
git commit -m 'fix the thing' --allow-empty

git push <your_github_username> HEAD
```
