# [what is PATH? (beginner - intermediate)](https://youtu.be/ZpOoRSkm-dQ)

Today I talk about PATH and how executables are found!

## Interactive examples

### Bash

```bash
echo $PATH

touch a:b
ls

rm a:b
ls

ls ~/
which python
which -a python

virtualenv venv
. venv/bin/activate

echo $PATH
which -a python

mkdir bin
echo 'echo hi' > bin/t
chmod +x !$
export PATH="$PWD/bin:$PATH"
t

export PATH="$PWD/bin"
ls
```
