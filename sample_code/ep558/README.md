# [git: --first-parent (intermediate)](https://youtu.be/nsSj7snqODM)

Today we talk about a helpful argument in `git` for visualizing histories (and diffs!)

## Interactive examples

### Bash

```bash
git clone git@github.com:anthonywritescode/twitch-chat-bot
cd twitch-chat-bot/

git log
git log --oneline
git log --oneline --graph

git show <commit_hash>
git log --oneline --first-parent
git show --first-parent <commit_hash>

git clone git@github.com:pre-commit/pre-commit
cd pre-commit/
git log --oneline --first-parent --decorate
```
