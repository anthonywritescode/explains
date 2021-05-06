# [SUPER FAST cpython with mypyc (intermediate)](https://youtu.be/0Cjg3qvHBEY)

Today I show how you can make your python super fast just by passing it through `mypyc`!

## Interactive examples

### Bash

```bash
# git clone https://github.com/anthonywritescode/aoc2020

babi part2.py
python3 -m part2 input.txt

virtualenv venv
. venv/bin/activate
pip install mypy

mypyc part2.py
ls
python -c 'import part2; part2.main()'
pypy3 part2.py
```
