# [git workflow: branch name collisions (intermediate)](https://youtu.be/XHU3Kvudraw)

Today I talk about the workflow I use when dealing with many remotes with conflicting branch names.  P.S. please don't make pull requests from a branch named "master"!

## Setup commands

```bash
git clone git@github.com:pre-commit/pre-commit
# git clone https://github.com/pre-commit/pre-commit
cd pre-commit
```

## Interactive examples

### Bash

```bash
git remote -v
git branch -r

git checkout demo
# git checkout <demo_branch_name>

git checkout allow_ci_key
# git checkout <ambiguous_branch_name>

git checkout asottile/allow_ci_key -b asottile__allow_ci_key
# git checkout <remote_name>/<ambiguous_branch_name> -b <remote_name>__<ambiguous_branch_name>

git log
git status

git commit -m 'hello world' --allow-empty
git push asottile HEAD:allow_ci_key
# git push <remote_name> HEAD:<ambiguous_branch_name>
```
