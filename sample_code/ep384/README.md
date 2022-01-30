# [dropping old python versions (intermediate)](https://youtu.be/Oun5kXqENMk)

Today I show how I drop old python versions, some tools you can use to automatically do some of the work, and why I only bump the minor version!

## Interactive examples

### Bash

```bash
# git clone https://github.com/asottile/covdefaults
git clone git@github.com:asottile/covdefaults
cd covdefaults/

git grep 3.*6
nano setup.cfg
nano tox.ini
nano azure-pipelines.yml

git grep 3.*7

nano .pre-commit-config.yaml
pre-commit run --all-files

git add -u
git status
```
