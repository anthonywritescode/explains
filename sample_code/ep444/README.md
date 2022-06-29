# [what is gbp? (intermediate - advanced)](https://youtu.be/Nu4TIETrktY)

Today I walk through `gbp` "git-buildpackage" -- a tool that I use for debian packaging (deadsnakes and more!)

## Interactive examples

### Bash

Session 1:

```bash
git init tmux-jammy-2
cd tmux-jammy-2/

gbp import-dsc --allow-unauthenticated --create-missing-branches --upstream-branch upstream --pristine-tar --debian-branch=ubuntu/jammy http://archive.ubuntu.com/ubuntu/pool/main/t/tmux/tmux_3.2a-4build1.dsc

git branch
git show pristine-tar
git status

# git branch -m ubuntu/jammy

gbp pq import
git branch

gbp pq export
git status
git diff

git add -u
git commit -m 'refresh patches'

git checkout patch-queue/ubuntu/jammy
git log --oneline
git show <commit_hash>
git diff <commit_hash>^ <commit_hash>

ls debian/patches/

git remote add upstream git@github.com:tmux/tmux
git fetch upstream
git cherry-pick <commit_hash>
git show

gbp pq export
git status
git diff -- debian/patches/series
git add debian/
git commit -m 'upstream commit <commit_hash>'

dch -v 3.2a-4build1+asottile1
git status
git add debian/
git commit -m 'finish changelog for 3.2a-4build1+asottile1'

# gbp buildpackage -us -uc --git-pristine-tar --git-debian-branch=ubuntu/jammy

cd ..
git clone git@github.com:deadsnakes/runbooks
cd -

../runbooks/build
ls ../dist/

docker run -v $PWD/../dist:/dist:ro -ti ubuntu:jammy bash
ls /dist/

apt update
apt install /dist/tmux_3.2a-4build1+asottile1_amd64.deb
# Ctrl-d
exit


```

Session 2:

```bash
# gbp buildpackage --git-builder='debuild -S' --git-pristine-tar -git-debian-branch=ubuntu/jammy
../runbooks/build --source
rm -rf ../dist/
../runbooks/build --source
ls ../dist/

cd ../dist/
dput ppa:asottile/tmux-jammy *_source.changes

cd ..
wget https://github.com/tmux/tmux/releases/download/3.3a/tmux-3.3a.tar.gz

cd tmux-jammy-2/
gbp import-orig ../tmux-3.3a.tar.gz --pristine-tar --no-interactive --no-symlink-orig --no-merge

git log upstream
git branch
git merge upstream

gbp pq rebase
git status

nano tmux.c
git add !$
git rebase --continue

git status
nano configure.ac
git rebase --continue
```
