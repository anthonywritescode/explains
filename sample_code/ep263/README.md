# [move a virtualenv! (intermediate)](https://youtu.be/iZlgLrWed1I)

Today I show how to move a virtualenv, and why it doesn't work by default!

## Interactive examples

### Bash

```bash
virtualenv src
src/bin/pip install astpretty
./src/bin/astpretty --help
./src/bin/astpretty /dev/stdin <<< 'print("hello world")'

ls
mv src/ dest
./dest/bin/astpretty
nano dest/bin/astpretty
nano dest/bin/activate

virtualenv venv
. venv/bin/activate
pip install virtualenv-tools3

virtualenv-tools --help
virtualenv-tools dest/ --verbose --update-path auto
./dest/bin/astpretty --help
. ./dest/bin/activate
echo $VIRTUAL_ENV
```
