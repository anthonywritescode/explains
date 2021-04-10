# [git rebase (and git rebase -i) (intermediate)](https://youtu.be/hv8dhOEzQcM)

Today I talk about "what is rebasing" and the various options to interactive rebasing (the git chainsaw as I call it)

## Interactive examples

### Bash

```bash
git clone git@github.com:pre-commit/pre-commit-hooks
# git clone https://github.com/pre-commit/pre-commit-hooks

cd pre-commit-hooks/
git remote add <remote_name> git@github.com:<username>/pre-commit-hooks
git fetch <remote_name>
git checkout <remote_name>/master -b <username>_master
git branch -u origin/master
git status

git reflog
git rebase -i origin/master
git log

git rebase -i origin/master
git show
git rebase --continue

git rebase -i origin/master
git status
git push <remote_name> HEAD:master
git push <remote_name> HEAD:master -f
```
