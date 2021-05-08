# [updating a forked repository (beginner - intermediate)](https://youtu.be/MSYqb9EWjto)

Today I show the procedure for updating the main branch of a forked repository.  I also show my workflow which ~generally doesn't require such a procedure!

## Interactive examples

### Bash

Session 1:

```bash
git clone git@github.com:<username>/pyflakes
# git clone https://github.com/<username>/pyflakes

cd pyflakes/
git log
git status
git remote -v

git remote add upstream git@github.com:pycqa/pyflakes
git fetch upstream

git branch
git merge upstream/master --ff-only
git log
git status

git remote -v
git push origin HEAD
```

Session 2:

```bash
rm -rf pyflakes/
git clone git@github.com:pycqa/pyflakes
cd pyflakes/

git remote add <username> git@github.com:<username>/pyflakes
git fetch <username>
git checkout origin/master -b new_branch
git log
git remote -v

cd ..
rm -rf pyflakes/
git clone git@github.com:pycqa/pyflakes
cd pyflakes/

git github-fork
git remote -v
```
