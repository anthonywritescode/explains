# [how I sped up python's tokenize module by 25% (intermediate)](https://youtu.be/fYbeK47C5b8)

Today I show how I went about improving the performance of the tokenize module by 20-30%.  first why I noticed it at all to begin with

## Setup commands

```bash
virtualenv venv
. venv/bin/activate
pip install add-trailing-comma babi gprof2dot

git clone git@github.com:python/cpython
# git clone https://github.com/python/cpython
```

## Interactive examples

### Bash

Session 1:

```bash
time add-trailing-comma old.py
time add-trailing-comma old.py old.py old.py
python -m cProfile -o out.pstats -m add-trailing-comma old.py old.py old.py
gprof2dot out.pstats | dot -Tsvg -o out.svg
firefox out.svg &
gprof2dot -z _main:57:fix_file out.pstats | dot -Tsvg -o out.svg
```

Session 2:

```bash
cd cpython
./configure && make -j4

git ls-files -z -- '*.py' | xargs -0 wc -l | sort -rn | head -5

./python -m cProfile -o out.pstats -m t
gprof2dot out.pstats | dot -Tsvg -o out.svg
firefox out.svg &

babi Lib/tokenize.py

./python -m cProfile -o out.pstats -m t
gprof2dot out.pstats | dot -Tsvg -o out2.svg
firefox out.svg &

time ./python -c 'import tokenize'
git checkout -- .
time ./python -c 'import tokenize'

babi Lib/tokenize.py

./python -m cProfile -o out.pstats -m t
gprof2dot out.pstats | dot -Tsvg -o out3.svg
firefox out.svg &
```
