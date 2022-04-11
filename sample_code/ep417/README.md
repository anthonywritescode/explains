# [how I sped up python by 20ms (intermediate)](https://youtu.be/kI9WjDNxRJM)

Today I show the tools and processes I used to improve python startup in virtualenvs!

## Interactive examples

### Bash

Session 1:

```bash
python -Ximporttime -c ''
python -S -Ximporttime -c ''
time python -c ''

virtualenv venv
. venv/bin/activate
time python -c ''

virtualenv venv310 -p python3.10
.venv310/bin/activate
time python -c ''
python -Ximporttime -c ''

pip install importtime-waterfall

touch t.py
importtime-waterfall t
importtime-waterfall --include-interpreter-startup t
importtime-waterfall t --include-interpreter-startup --har | xclip -selection c
```

Session 2:

```bash
time python3.10 -c ''

nano venv/lib/python*/site-packages/_virtualenv.py
nano venv310/lib/python*/site-packages/_virtualenv.py
```
