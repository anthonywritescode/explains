# [pathlib is slow? how I improved black's caching by 40x (intermediate)](https://youtu.be/tFrh9hKMS6Y)

Today I show how replacing pathlib with plain strings speeds up black's cache by a rather significant amount!

## Interactive examples

### Bash

```bash
virtualenv venv
. venv/bin/activate
pip install black

ls -alh ~/.cache/black/*
black t.py
time black t.py
ls

mkdir t
rm -rf t && time XDG_CACHE_HOME=$PWD/t black t.py

python -m cProfile -o log.pstats -m black t.py

pip install yelp-gprof2dot
gprof2dot log.pstats | dot -Tsvg -o log.svg
gprof2dot -z <node_identifier> log.pstats | dot -Tsvg -o log.svg
```
