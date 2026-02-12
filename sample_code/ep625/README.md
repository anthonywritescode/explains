# ["new" git commands for "old" people](https://youtu.be/10dQiNkCZGE)

today I show the equivalent `checkout` / `reset` commands with `switch` / `restore`!

## Setup commands

## Interactive examples

### Bash

```bash
git clone git@github.com:assotile/astpretty
cd astpretty/

git branch

git checkout origin/main -b my-feature-branch
git switch origin/main -c my-feature-branch2

git branch
git status

git switch my-feature-branch
git checkout my-feature-branch2

git switch -
git checkout -

git branch -r

cd ..
git clone git@github.com:asottile/all-repos
cd all-repos/

git branch -r
git branch

git checkout all-repos-scripts  # git checkout origin/... -b ...
git branch

git branch -u origin/main
git status

git checkout main
git branch -D all-repos-scripts

git switch all-repos-scripts
git switch --help

git tag -l
git checkout v1.2.0
git status

git checkout HEAD^^^^
git status
git branch

git switch --detach HEAD^^^^
git switch HEAD^^^^

git checkout --orphan newbranch
git status
git log
git branch

git reset .
git commit --allow-empty -m 'empty initial commit'
git commit -n --allow-empty -m 'empty initial commit'

git log
git branch

git clean -fxfd
git checkout main

git switch --orphan newbranchname2
git status
git log

git branch
git branch --show-current

git checkout main
git status

echo -e '\n' >> setup.py
echo 'hello hello' >> README.md
echo "print('hi')" >> all_repos/clone.py

git status
git checkout -- README.md
git status

git restore -- setup.py
git status
git restore -- .
git status

echo -e '\n' >> setup.py
echo -e '\n' >> README.md
echo -e '\n' >> all_repos/clone.py

git checkout -p
git status

echo -e '\n' >> setup.py
echo -e '\n' >> all_repos/clone.py
git status

git restore -p
git status

git tag -l
git checkout v1.29.0 -- .pre-commit-config.yaml setup.cfg
git status

nano setup.cfg
git diff --staged

git reset -- .pre-commit-config.yaml setup.cfg
git restore -- .pre-commit-config.yaml setup.cfg

git restore --source v1.29.0 -- .pre-commit-config.yaml setup.cfg
git status

nano setup.cfg
git diff !$
git status

git restore --staged --worktree --source v1.29.0 -- .pre-commit-config.yaml setup.cfg
git status
git diff --staged

git restore --staged -- setup.cfg
git status

git diff -- setup.cfg
git add setup.cfg
git status

git restore --staged --worktree -- setup.cfg
git status

git restore --staged -p
git restore --staged -- .
git restore -- .
git status

git branch
git rev-parse HEAD

git reset --hard v1.19.0
git status
git rev-parse HEAD

git reset --hard origin/main
git status

git reset --soft HEAD^^^^^
git status

git rev-parse HEAD
git diff --staged
git status
```
