# [pathlib is slow! falsey is tricky! (pytest bug) (intermediate - advanced)](https://youtu.be/qiZyDLEJHh0)

Today I show how I triaged and ultimately fixed a big performance regression in pytest!  I walk through the tools and techniques I used and show a few general programming tips

## Interactive examples

### Bash

```bash
# git clone git@github.com:podhmo/python-node-semver
git clone https://github.com/podhmo/python-node-semver

virtualenv venv6
virtualenv venv7

# venv6/bin/pip install pytest==6.2.5
venv6/bin/pip install pytest
# venv7/bin/pip install pytest==7.0.0rc1
venv7/bin/pip install pytest --pre

cd python-node-semver/
../venv6/bin/python -m pytest nodesemver/
../venv7/bin/python -m pytest nodesemver/

../venv7/bin/python -m cProfile -o log.pstats -m pytest nodesemver/
ls log.pstats

../venv7/bin/pip install yelp-gprof2dot
../venv7/bin/gprof2dot log.pstats | dot -Tsvg -o out.svg
firefox out.svg &

../venv7/bin/gprof2dot --help
../venv7/bin/gprof2dot -n 1 -e .5 log.pstats | dot -Tsvg -o out.svg
firefox out.svg &

cd ..
git clone git@github.com:pytest-dev/pytest
cd pytest/

timeout --help
virtualenv venv
. venv/bin/activate

pip install -e .
pip install toml

nano t.sh
chmod +x t.sh

git bisect start
git bisect good 6.2.5
git bisect bad 7.0.0rc1
git bisect run ./t.sh
```
