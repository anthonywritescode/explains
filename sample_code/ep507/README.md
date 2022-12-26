# [don't git clone over https! (beginner)](https://youtu.be/5o9ltH6YmtM)

In today's video I talk about git cloning when you want to make a contribution and present the benefits of using an ssh key -- I also show how to set one up

## Interactive examples

### Bash

```bash
git clone https://github.com/asottile/astpretty
cd astpretty/

git checkout origin/main -b wat
nano README.md
# echo 'hello hello wolrd' >> README.md

git commit -m 'hello hello wolrd'
git push origin HEAD

cd ..
rm -rf astpretty/

git clone git@github.com:asottile/astpretty
cd astpretty/

ssh-keygen -t ed25519 -C asottile@umich.edu
ls ~/.ssh/

cat ~/.ssh/id_ed25519.pub
ssh-add

git clone git@github.com:asottile/astpretty
cd astpretty/

git checkout origin/main -b wat
nano README.md
# echo 'hello hello wolrd' >> README.md

git push origin HEAD
```
