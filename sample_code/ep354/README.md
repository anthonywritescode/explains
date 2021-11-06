# [git without `cd` (intermediate)](https://youtu.be/fQ3-Y99Fzro)

Today I show a very quick trick for running git commands in other directories without requiring `cd`!

## Interactive examples

### Bash

```bash
git init pre-commit
git init all-repos
cd pre-commit/
git status

git -C ../all-repos/ status
```
