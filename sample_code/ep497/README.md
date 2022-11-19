# [git is just a key value store? (advanced)](https://youtu.be/HvA-WkXqlDI)

Today we dive into the low level representation of how git works!  turns out it's mostly just a fancy blob store!

## Interactive examples

### Bash

```bash
git clone git@github.com:asottile/astpretty
cd astpretty/

ls
ls .git
ls .git/objects/ -al

git cat-file -p HEAD:setup.py
git rev-parse HEAD:setup.py
git cat-file -p <hash>

git hash-object -w setup.py
sha1sum setup.py

mkdir foo
git add foo
git status
git cat-file -p HEAD:
git cat-file -p <hash>

chmod +x setup.py
git add setup.py
git write-tree
git cat-file -p <hash>

git cat-file --batch <<< <hash>
git cat-file -p <hash>

git rev-parse HEAD
git hash-object -w <<EOF
    <content>
EOF
```
