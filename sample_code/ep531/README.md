# [rerunning github checks (beginner - intermediate)](https://youtu.be/OYh22O1B5D0)

So your tests failed... they're definitely a flake right? here's a few ways to retry them even if you don't have commit access to the repo!

## Interactive examples

### Bash

```bash
git status

git commit --amend --no-edit
git remove -v
git push origin HEAD -f

git commit --allow-empty -m 'trigger CI'
git push origin HEAD
```
