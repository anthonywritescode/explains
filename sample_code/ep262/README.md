# [what is the XDG base directory specification? (intermediate)](https://youtu.be/wT85Ynk-0MY)

Today I talk about the XDG base directory specification and how an application might go about adhering to it (as well as some cool things you can do to manipulate apps that work with it!)

## Interactive examples

### Bash

```bash
echo $XDG_RUNTIME_DIR
git clone git@github.com:asottile/astpretty
# git clone https://github.com/asottile/astpretty
cd astpretty/

pre-commit install-hooks
ls ~/.cache/pre-commit
ls ~/ -al

XDG_CACHE_HOME=$PWD/cache pre-commit install-hooks
ls cache
ls cache/pre-commit
cat cache/pre-commit/README
```
