# [git: visualizing main line commits (intermediate)](https://youtu.be/UjCnvh6uAUs)

Today I show a few useful options to `git log` to help visualize the commit history: --decorate, --oneline, --graph, --first-parent, as well as their combinations!

## Setup commands

```bash
git clone git@github.com:pre-commit/pre-commit
# git clone https://github.com/pre-commit/pre-commit
cd pre-commit
```

## Interactive examples

### Bash

```bash
git log
git log --decorate
git log --oneline
git log --oneline --graph
git log --oneline --first-parent
git log --oneline --first-parent --graph
```
