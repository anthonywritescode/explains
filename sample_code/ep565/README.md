# [git: inline diffs with --word-diff! (intermediate)](https://youtu.be/Wn3bJUzvy5I)

Today I show a tiny tip when working with patches in `git` (such as with `git diff` or `git log -p`) to show inline differences instead of full line differences

## Interactive examples

### Bash

```bash
git log --format= -p devenv/config.ini
git log --word-diff --format= -p devenv/config.ini

git log --word-diff-regex '[^[:space:]]' --word-diff --format= -p devenv/config.ini
git log --word-diff-regex '[a-f0-9]+|[^[:space:]]' --word-diff --format= -p devenv/config.ini
git log --word-diff-regex '[0-9]+|[a-f0-9]+|[^[:space:]]' --word-diff --format= -p devenv/config.ini
```
