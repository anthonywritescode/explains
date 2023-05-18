# [you can't always trust argv\[0\] (intermediate)](https://youtu.be/qwpfSL-AcFQ)

Today I explain what `argv[0]` is -- and then how it can't always be trusted due to the way `exec` works!

## Interactive examples

### Python

```python
import os

os.execvp('./a.out', ['bogus', 'args', 'here'])
```

### Bash

```bash
babi t.c
gcc t.c

./a.out
$PWD/a.out

ln -s a.out some-exe
./some-exe
$PWD/some-exe

python

git clone --depth=1 git@github.com:asottile/rename-exchange
nano rename-exchange/test.sh

git clone --depth=1 git@github.com:pre-commit/pre-commit
nano pre-commit/pre_commit/resources/hook-tmpl
```
