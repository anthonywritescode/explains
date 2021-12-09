# [making your own custom git commands (intermediate)](https://youtu.be/YwG8C0jPapE)

Today I go over two different ways to make your own `git` subcommands!

## Interactive examples

### Bash

```bash
git init repo
cd !$

nano ~/.gitconfig

git comit --allow-empty -m 'foo'
git git git git git git status

git c --allow-empty -m 'foo'
git wat
git wat wat wat wat

git shell --help

# git clone https://github.com/pycqa/flake8
git clone git@github.com:pycqa/flake8
cd flake8/
git github-url
git github-fork
git remote -v

ls ~/bin/
echo $PATH

cd ../../
mkdir bin
nano bin/git-hello-world
chmod +x !$

export PATH=$PWD/bin:$PATH
which git-hello-world
git hello-world
git hello-world anthony
```
