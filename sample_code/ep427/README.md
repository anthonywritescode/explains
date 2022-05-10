# [I made pip startup 25% faster (intermediate)](https://youtu.be/GmK1So7F0ZQ)

Today I show how I tracked down a performance regression, how I fixed it, and ultimately how it made pip way faster!

## Interactive examples

### Bash

```bash
git clone git@github.com:pyparsing/pyparsing
# git clone https://github.com/pyparsing/pyparsing
cd pyparsing/

virtualenv venv -ppython3.10
. venv/bin/activate
pip install -e .

git tag -l | grep 2.4.7
git checkout pyparsing_2.4.7
time python -c 'import pyparsing'

git checkout pyparsing_3.0.0
time python -c 'import pyparsing'

git bisect start
git bisect good pyparsing_2.4.7
git bisect bad pyparsing_3.0.0
git bisect run python t.py --cutoff .09

git show <commit_hash>

git bisect reset
git bisect start
git bisect good pyparsing_2.4.7
git bisect bad pyparsing_3.0.0
git bisect run python t.py --cutoff .12
```
