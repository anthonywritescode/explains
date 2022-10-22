# [hiding your email on github (beginner)](https://youtu.be/O3e19cwX6uY)

Today I show a technique that you can use to hide your email in your git commits.  I also show a useful trick to get the email for every account including bots and apps!

## Interactive examples

### Bash

```bash
git clone git@github.com:<username>/throwaway
cd throwaway

git commit --allow-empty -m 'some commit message'
nano ~/.gitconfig

git show --format='%ae'
git show --format='%ce'

git branch -m main
git push origin HEAD

git config --global user.email <email>

git commit --allow-empty -m 'some commit message 2'
git show --format='%ce'
git push origin HEAD

echo 'hello wolrd' > t
git add t
git commit -m 'add t'
git push origin HEAD

git -c user.name='github actions' -c user.email='<email>' commit --allow-empty -m 'some message'
git push origin HEAD
```
