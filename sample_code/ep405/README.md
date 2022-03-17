# [why does `cd --` go to ~ ? (intermediate)](https://youtu.be/vrIsG0Rw5xY)

Today I show a quirk of `cd --` and explain why `--` goes to the home directory! (as opposed to `cd -`)

## Interactive examples

### Bash

```bash
mkdir a

cd a
cd -

cd --
pwd

cd -
cd --
cd -

mkdir -foo
mkdir -- -foo
mkdir ./-bar

cd -foo
cd -- -foo
cd

git init wat
cd !$

ls
touch './~ -rf'
git status

rm './~ -rf'
ls ~
cd --
```
