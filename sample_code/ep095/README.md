# [git: commit message pro tip (beginner - intermediate)](https://youtu.be/CWrBZeC2Qqs)

Today I talk about a little tip I stumbled upon for making better git commit messages!

## Interactive examples

### Bash

```bash
git init repo
cd !$

git commit --allow-empty -m 'some commit message'
git show

git commit --allow-empty
git show

git commit --allow-empty -m 'first line here' -m 'body message here'
git show

git commit --allow-empty -m 'first line here' -m 'body message here' -m 'hello world'
git show
```
