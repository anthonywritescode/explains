# [pretty python profiling (intermediate)](https://youtu.be/ey_P64E34g0)

Today I show how I figure out what's slow in a python application and some cool visualization tools!

## Setup commands

```bash
virtualenv venv

. venv/bin/activate

pip install pre-commit

pip install importtime-waterfall

pip install yelp-gprof2dot
```

## Interactive examples

### Bash

```bash
pre-commit run

time python -c 'import pre_commit.main'

importtime-waterfall pre_commit.main
importtime-waterfall pre_commit.main --har
importtime-waterfall pre_commit.main --har | xclip -selection c

python -m cProfile --help
python -m cProfile -o log.pstats $(which pre-commit) run
python -m cProfile -o log.pstats -m pre_commit.main run

head -c 20 log.pstats

python -m pstats log.pstats

gprof2dot --help
gprof2dot log.pstats | vi
gprof2dot log.pstats | dot -Tsvg -o log.svg
gprof2dot log.pstats -z main:181:main | dot -Tsvg -o log.svg
```
