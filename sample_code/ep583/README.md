# [stop making giant changesets!](https://youtu.be/Gu6XrmfwivI)

and a workflow I use to split a changeset into many small easily-reviewable changesets!

## Setup commands

```bash
git clone git@github.com:getsentry/sentry
cd sentry
```

## Interactive examples

### Bash

```bash
git log --oneline --decorate
git branch
git branch -D <branch_name>

git checkout origin/master -b <branch_name>
git cherry-pick <commit_hash>

git branch
git checkout <branch_name>

git fetch
git rebase -i origin/master
git status

git branch
git checkout <branch_name>

nano README.md
git status
git add -u
git commit --amend --no-edit

git checkout <branch_name>
git rebase -i <branch_name>

git checkout <branch_name>
git rebase -i origin/master
git checkout <branch_name>
git rebase -i <branch_name>
git status
git rebase --continue

git log --oneline --decorate
git rebase -i origin/master
```
