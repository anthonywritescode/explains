# ["git is forever"](https://youtu.be/krjqA-oBgxI)

so stop doing these two things!

## Setup commands

```bash
git clone git@github.com:pre-commit/pre-commit
```

## Interactive examples

### Bash

```bash
cd pre-commit/

git log --reverse
git show <commit_hash>:pre-commit.py

cd -
du -hs  .git

chmod +x t.sh
./t.sh
git cat-file blob <hash> | less
```
