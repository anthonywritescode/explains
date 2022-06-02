# [a git workflow for *only my branches* (intermediate)](https://youtu.be/GKBq5Xo_B6I)

Today I show off a git workflow I use when I'm working on a repository with hundreds or thousands of other branches (such as at work!)

## Interactive examples

### Bash

```bash
git clone git@github.com:getsentry/sentry
cd sentry/

git branch -r
git branch -r | wc -l
git branch -r | grep asottile

git fetch
babi .git/config

# https://github.com/asottile/scratch/wiki/only-track-my-branches

git fetch --all --prune
git rev-parse --abbrev-ref origin/HEAD | cut -d/ -f2-
git rev-parse --abbrev-ref origin/HEAD
git config remote.origin.fetch "+refs/heads/master:refs/remotes/origin/master"
babi .git/config
git fetch

git config --add remote.origin.fetch "+refs/heads/$USER-*:refs/remotes/origin/$USER-*"
babi .git/config
git fetch

git for-each-ref
git for-each-ref | awk '{print $3}'
git for-each-ref | awk '{print $3}' | grep -Ev "^(refs/heads/|refs/remotes/origin/(HEAD$|master$|${USER}-))"
git for-each-ref | awk '{print $3}' | grep -Ev "^(refs/heads/|refs/remotes/origin/(HEAD$|master$|${USER}-))" | xargs -n1 git update-ref -d

git branch -r
git fetch

git for-each-ref | awk '{print $3}' | grep -Ev "^(refs/heads/|refs/tags|refs/remotes/origin/(HEAD$|master$|${USER}-))" | xargs --no-run-if-empty -n1 git update-ref -d
git fetch

git fetch origin <branch>
git checkout FETCH_HEAD -b <branch>
git log
```
