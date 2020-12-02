# [python github actions w/ tox and pre-commit (intermediate)](https://youtu.be/KKJL8bM4cis)

Today I show how to set up a basic github actions workflow for testing a python project with pre-commit and tox!

## Setup commands

```bash
virtualenv venv

. venv/bin/activate

pip install pre-commit tox

# first you need to fork or create a new git repo via GitHub
git clone git@github.com:<your_github_username>/add-trailing-comma
```

## Interactive examples

### Bash

```bash
cd add-trailing-comma
pre-commit run --all-files

mkdir -p .github/workflows
git add .github/
git commit -m "add github action for pre-commit"
git push origin HEAD

tox -e py37
tox -e py

git add .github/
git commit -m "add workflow for running tox"
git push origin HEAD

git add -u
git commit --amend && git push origin HEAD -f
```
