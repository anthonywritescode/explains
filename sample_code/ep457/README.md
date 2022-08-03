# [how I made my import sorter 7x faster (intermediate)](https://youtu.be/Q3menOSxRC4)

And I actually went a bit further after recording!  (it now can reorder all of pre-commit faster than `isort` can import!

## Interactive examples

### Bash

```bash
git clone git@github.com:pre-commit/pre-commit
cd pre-commit/

virtualenv venv
. venv/bin/activate
pip install reorder-python-imports==3.1.0

best-of -- reorder-python-imports --py37-plus $(git ls-files -- '*.py')
best-of -- reorder-python-imports $(git ls-files -- '*.py')
best-of -- python3 -c 'import reorder_python_imports'

python prof.py reorder-python-imports --py37-plus $(git ls-files -- '*.py')
pip install yelp-gprof2dot
gprof2dot out.pstats | dot -Tsvg -o out.svg
firefox out.svg &

git clone git@github.com:asottile/reorder_python_imports
cd reorder_python_imports/
git checkout v3.1.0

cd ..
pip install reorder-python-imports --upgrade
best-of -- reorder-python-imports --py37-plus $(git ls-files -- '*.py')

python prof.py reorder-python-imports --py37-plus $(git ls-files -- '*.py')
gprof2dot out.pstats | dot -Tsvg -o out2.svg
firefox out2.svg &
```
