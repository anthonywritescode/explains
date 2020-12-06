# [git: ignoring noisy whitespace changes (beginner - intermediate)](https://youtu.be/qYJWBJvHqj0)

Today I show how to ignore noisy whitespace changes in git so you can focus on the actually important things!  Also show some tips for how to utilize this on github as well.

## Setup commands

```bash
git clone git@github.com:pre-commit/action
```

## Interactive examples

### Bash

```bash
git remote
git remote -v
git show
git blame webpack.config.js
git show --help
git show 771019abd66cc479f5d970869d778ec7ed488a89 -w
git blame -w webpack.config.js
git blame -M3 -w webpack.config.js
```
