# [how to make a simple github PR (beginner)](https://youtu.be/cysuuUtbC6E)

Today I show the process I use to make pull requests to projects!  I walk through the git commandline and make a small typo fix to an open source project!

## Interactive examples

### Bash

```bash
git clone git@github.com:<your_github_username>/<repository_name>
cd <repository_name>/
git branch

git checkout origin/master -b fix_typo
git branch

# make changes
git diff
git diff --word-diff

git status
git add <name_of_changed_file>
git status
git commit -m "Fixed typo in <name_of_changed_file>"

git branch
git status
git push origin HEAD
# git push origin fix_typo
```
