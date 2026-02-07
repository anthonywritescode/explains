# [git is not a series of patches!](https://youtu.be/LI6Zzl787KU)

today I talk about an intuition I had wrong about git!

## Interactive examples

### Bash

```bash
git clone git@github.com:asottile/astpretty
cd astpretty/

ls
git branch
git rev-parse main
git ls-remote

git cat-file commit <commit_hash>
git cat-file commit <commit_hash> | wc -c

(echo -en 'commit 1188\0' && git cat-file commit <commit_hash>) | sha1sum

git log --oneline --decorate | head -10
git log --graph --oneline --decorate | head -10

git cat-file commit <commit_hash>
git cat-file commit <commit_hash> | head -10

git cat-file tree <hash>
git cat-file -p <hash>

git cat-file tree <hash> | wc -c
(echo -en '423\0' && git cat-file tree <hash>) | sha1sum

git cat-file -p <hash>
git cat-file blob <hash>

cd ..
git clone git@github.com:sass/libsass-python
cd libsass-python/

git cat-file commit HEAD
git rev-parse HEAD

git cat-file commit <commit_hash>
git cat-file -p <commit_hash>
git submodule update --init

cd ../astpretty/
git log -p --first-parent

git cat-file commit HEAD | grep tree && git cat-file commit <commit_hash> | grep tree
git diff-tree <hash> <hash>
git diff-tree -p <hash> <hash>
```
