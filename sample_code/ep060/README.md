# [git show (+ some tips!) (beginner)](https://youtu.be/gFKgEbbQRyQ)

Today I show how to use `git show` as well as some helpful tips for some specialized situations!

## Interactive examples

### Bash

```bash
git log
git show <commit_hash>
git show
git show HEAD
git show -m HEAD
git tag -l
git show <tag_string>
git show --name-only <tag_string>
nano $(git show --name-only <tag_string>)
git show --name-only --format= <tag_string>
git show HEAD^^^^
git show -m HEAD^^^^
```
