# [github: give people credit! (beginner - intermediate)](https://youtu.be/_-qNX8EbVYI)

Today I show a technique for giving other contributors credit for git commits!  especially useful for pair programming situations

## Interactive examples

### Bash

```bash
# git clone https://github.com/<username>/test-repo-plz-ignore
git clone git@github.com:<username>/test-repo-plz-ignore
cd test-repo-plz-ignore/

git commit -m 'foo' --allow-empty
git push origin HEAD

nano ~/.gitconfig

git commit --allow-empty -m 'this is the new message' -m 'Co-authored-by: Chris Kuehl <ckuehl@ckuehl.me>'
git push origin HEAD

git commit --allow-empty \
    -m 'a third commit' \
    -m 'Co-authored-by: deadsnakes whatever <34804342+deadsnakes-issues-bot@users.noreply.github.com>'
git push origin HEAD

git commit --amend --allow-empty \
    -m 'a third commit' \
    -m 'Co-authored-by: deadsnakes whatever <34804342+deadsnakes-issues-bot@users.noreply.github.com>' \
    -m 'Co-authored-by: Chris Kuehl <ckuehl@ckuehl.me>'
```
