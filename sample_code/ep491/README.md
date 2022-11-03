# [avoid notification spam with draft PRs! (beginner)](https://youtu.be/LOLpOTYzknI)

Today I show a quick github trick to avoid embarrassment with github pull requests!

## Interactive examples

### Bash

```bash
# git clone ...
git push origin HEAD

nano main.mjs
git add -u
git commit --amend --no-edit && git push origin HEAD -f
```
