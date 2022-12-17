# [git: the several ways to "--sign" (intermediate)](https://youtu.be/6hu3cbBhHqQ)

Today I talk about the two ways that "signatures" are added during git commits / tags as well as how they are actually implemented!

## Interactive examples

### Bash

```bash
git clone git@github.com:asottile/astpretty
cd astpretty/

git checkout origin/main -b my-branch
git commit --allow-empty -m 'hello world' --signoff

git cat-file -p <commit_hash>
git show <commit_hash>

git commit --amend --allow-empty
git show

git commit --allow-empty -m 'hello world' --gpg-sign
git show

git cat-file -p <commit_hash>

git commit --allow-empty -m 'hello world' --gpg-sign --signoff
git show HEAD
```
