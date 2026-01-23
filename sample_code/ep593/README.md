# [python is too slow...](https://youtu.be/FFoeU3t-N4c)

... for a text editor?  I talk about the architecture of babi and how I made it "fast enough" and ultimately that "sometimes it doesn't matter if it's slow"

## Setup commands

```bash
virtualenv venv
. venv/bin/activate

git clone git@github.com:asottile/babi
cd babi
```

## Interactive examples

### Bash

```bash
time python3 -c ''
time python3 -S -c ''
time python3 -S -c 'import babi.main'

. venv/bin/activate
pip install identify

pip uninstall babi
pip install -e .

pip install identify --upgrade
python3 -c 'import identify'
python3 -c 'import identify.identify'
time python3 -c 'import babi.main'

babi --help
babi --perf-log log babi/screen.py
nano log

pip install yelp-gprof2dot
gprof2dot log.pstats | dot -Tsvg -o img.svg
xdg-open img.svg

git show
git show --first-parent
git show HEAD^ --first-parent
git show HEAD^^ --first-parent

git log --first-parent
git log --first-parent --oneline
git show <commit_hash> --first-parent
```
