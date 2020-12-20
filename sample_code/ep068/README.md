# [git cherry-pick (intermediate)](https://youtu.be/hmMrtfyb1vc)

Today I talk about the `git cherry-pick` command and several uses / workflows I use it for!

## Interactive examples

### Bash

```bash
git clone git@github.com:pytest-dev/pytest
# git clone https://github.com/pytest-dev/pytest

git log
git show <commit_hash>
git status

git checkout 5.4.x
git cherry-pick <commit_hash>
git show

git show <commit_hash>
git checkout 4.6.x
git cherry-pick <commit_hash>
git status

nano <filename>
git add !$
git status
git cherry-pick --continue

git checkout 5.4.x
git reset --hard origin/5.4.x

git log
git cherry-pick -m1 <commit_hash>
git show
```
