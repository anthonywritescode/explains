# [--argument prefix matching (beginner - intermediate)](https://youtu.be/jrs0l3HJ-Ow)

Today we talk about GNU long opts and prefix matching as well as how to disable it in python's argparse!

## Interactive examples

### Bash

```bash
git init --template= foo
cd foo/
ls

touch foo
git add foo
git commit --message 'this is the message'
git commit --mess 'this is a mess' --allow-empty

cd ..
rm -rf foo/

python t.py --name anthony
python t.py --n anthony
python t.py --na anthony

pre-commit run --help
pre-commit run --all-files
pre-commit run --all

git log -G --allow-
git log -p -G --allow-
```
