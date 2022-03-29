# [the fastest python startup with `python -S` (intermediate)](https://youtu.be/lCwz4S2vCH8)

Today I talk about the absolutely-fastest way to start python via `python -S` and why you generally don't ever want to use it!

## Interactive examples

### Python

```
import sys

sys.path

license
license()

help
exit
```

### Bash

```bash
virtualenv venv
. venv/bin/activate

python -X importtime -c ''

pip install importtime-waterfall
# echo "" > t.py
nano t.py
importtime-waterfall --include-interpreter-startup t

python
python -S

time python -c ''
time python -S -c ''
```
