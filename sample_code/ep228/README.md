# [the `install` command (beginner - intermediate)](https://youtu.be/Xk5XRy4OxOM)

Today I talk about the `install` command which I mostly use in Dockerfiles -- and no it doesn't have anything to do with package installation

## Interactive examples

### Bash

```bash
man install

install -d foo/bar/baz
tree foo

mkdir -p a/b/c
tree a

rm -r foo a

sudo install -d --owner=nobody --group=nogroup foo/bar/baz
ls -al
ls -al foo/bar/baz

sudo rm -r foo

mkdir -p foo/bar/baz
sudo chown nobody:nogroup foo/bar/baz
ls -al !$

touch a b c
mkdir dest
install a b c dest/
ls dest/

install --mode=0600 a b c dest/
ls -al dest/
```
