# [squash merge: I hate it but it's really the only way](https://youtu.be/5_8FTivl8Vs)

today we talk about merge strategies (again!) while specifically focusing on squash merge.  I show off a clever history rewriting technique to convert all merges into squashes!

## Interactive examples

### Bash

```bash
git log --oneline | wc -l
git log --oneline --all | wc -l

git log --format='%h %s' | grep -E '^[a-f0-9]+ .{1,7}$'
git log --format='%h %s' | grep -E '^[a-f0-9]+ .{1,7}$' | wc -l

virtualenv venv
. venv/bin/activate
pip install git-filter-repo

git clone git@github.com:asottile/pyupgrade
cd pyupgrade/

git log --oneline --graph
git show
git cat-file commit <commit_hash>
git cat-file commit <commit_hash>

git-filter-repo --help | less

bash ../t.sh
git log --oneline --graph --decorate | wc -l

git log --merges
git log --merges --oneline

cd ..
git clone git@github.com:jaseci-labs/jaseci --reference <directory> --dissociate
du -hs jaseci/.git

cd jaseci/
bash ../t.sh
git log --format='%h %s' | grep -E '^[a-f0-9]+ .{1,7}$' | wc -l
```
