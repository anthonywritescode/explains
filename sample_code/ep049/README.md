# [three ways to edit git commits (intermediate)](https://youtu.be/2LEn0GQJitM)

Today I go over three ways to edit commits with git to fix up issues or pretend like mistakes weren't made!

## Setup commands

```bash
git clone git@github.com:asottile/scratch
# git clone https://github.com/asottile/scratch

git clone git@github.com:asottile/scratch scratch2
# git clone https://github.com/asottile/scratch scratch2

git clone git@github.com:asottile/scratch scratch3
# git clone https://github.com/asottile/scratch scratch3

```

## Interactive examples

### Bash

```bash
# case 1
cd scratch
git show <commit_hash>
git status
git log
git add -u
git commit --amend

# case 2
cd ../scratch2
git log
git rebase -i <commit_hash>^
# edit commit
git status
git log
nano .gitconfig
git add !$
git commit --amend --no-edit
git rebase --continue
git log
git show <commit_hash>

# case 3
cd ../scratch3
git log
git show <commit_hash>
git rebase -i <commit_hash>^
# fixup commit
git log
```
