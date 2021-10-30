# [github wikis are repos! (beginner - intermediate)](https://youtu.be/U18COUDlzu8)

Today I show a neat trick for dealing with github wikis -- they're clonable as git repositories

## Interactive examples

### Bash

```bash
git clone git@github.com:asottile/scratch
# git clone https://github.com/asottile/scratch
cd scratch/
ls

git clone git@github.com:asottile/scratch.wiki
# git clone https://github.com/asottile/scratch.wiki
cd scratch.wiki/
ls

nano anthony-explains-ideas.md
git log -- !$
```
