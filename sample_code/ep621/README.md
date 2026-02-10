# [splitting a monorepo with git filter-branch / filter-repo](https://youtu.be/kBMTLIWkYVQ)

today we show how I split out a subsection of a monorepo to a separate repo while preserving history!

## Setup commands

```bash
git clone git@github.com:jaseci-labs/archived-jaseci jaseci-archived
virtualenv venv
venv/bin/pip install git-filter-repo
```

## Interactive examples

### Bash

```bash
cd jaseci-archived/
git rev-parse HEAD

ls jac/support/vscode_ext/jac/
git log -- '*/vscode_ext/*'
git log --name-only -- '*/vscode_ext/*' --oneline

git log --first-parent --name-only -- '*/vscode_ext/*' --oneline
bash t.sh
bash t2.sh

git -C jac-vscode-fb log --oneline
git -C jac-vscode-fb show <commit_hash>
git -C jac-vscode-fr log --oneline
```
