# [bash: pushd / popd (beginner - intermediate)](https://youtu.be/_cYaToOFml8)

Today I talk about pushd / popd and how it can be useful to change directories in an interactive shell and enter / exit contexts!

## Interactive examples

### Bash

```bash
mkdir -p foo/bar/baz
mkdir -p a/b/c

cd foo/bar/baz
touch foo
cd ../../../

pushd foo/bar/baz
ls
touch wat
popd

pushd foo
echo hi
echo hi > f
pushd bar
touch 2
pushd baz

# pushd /tmp/explains/a/b/c/
pushd `dirs +3 -l`/a/b/c
touch d

# popd +4
popd
popd
popd
popd

popd
```
