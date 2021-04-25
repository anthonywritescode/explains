# [what are git submodules? (intermediate)](https://youtu.be/RFcc-BQjCsE)

Today I talk about git submodules, what they are, how to add / change / delete them, and why you might use them!

## Interactive examples

### Bash

```bash
git init empty
cd !$
git commit --allow-empty -m 'empty initial commit'
git status
ls

git submodule add https://github.com/asottile/astpretty
git status

nano .gitmodules
git diff --staged
git commit -m 'add submodule for astpretty'

cd ..
git clone empty empty-clone
cd empty-clone/
git status
ls
ls astpretty/

cd ..
git clone empty empty-clone2 --recursive
cd empty-clone2/
ls astpretty/

cd ../empty-clone
git submodule update --init
git submodule update --init --recursive

cd astpretty/
git tag -l
git checkout v1.5.0
git status
git add astpretty
git diff --staged
git commit -m 'set astpretty to v1.5.0'

git rm astpretty/
git commit -m 'delete astpretty submodule'
git show

git clone git@github.com:sass/libsass-python
# git clone https://github.com/sass/libsass-python
cd libsass-python/

git submodule update --init
```
