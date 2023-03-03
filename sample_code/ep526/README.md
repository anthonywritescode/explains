# [my first rust open source PR (beginner - intermediate)](https://youtu.be/kIaOOYlbPWI)

Today I go over the approach I took to proposing a feature, implementing a feature, and ultimately getting it accepted to a new project!

## Interactive examples

### Python

```python
import hashlib
hashlib.sha1(b'blob 0\0').hexdigest()
hashlib.sha1(b'tree 0\0').hexdigest()
```

### Bash

```bash
# git clone git@github.com:Byron/gitoxide
# cd gitoxide/

git hash-object /dev/null
git grep empty_tree
git hash-object -t tree /dev/null

git checkout <commit_hash>^

git log --grep empty_tree
git log -G empty_tree
git log -G 'fn empty_tree'

git show <commit_hash>

sha1sum /dev/null
# printf 'blob 0\0' | sha1sum
sha1sum <<< $'blob 0\0'
```
