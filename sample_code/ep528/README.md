# [how I use git blame (beginner - intermediate)](https://youtu.be/8uuueHkWy-E)

Today I go over `git blame` -- how I use it, and how you can use the github UI as well for this!

## Interactive examples

### Bash

```bash
git rev-parse HEAD

git blame -w -M3 -- pre_commit/languages/dotnet.py
git show <commit_hash>

git blame <commit_hash>^ -w -M3 -- pre_commit/languages/dotnet.py
git show <commit_hash>
```
