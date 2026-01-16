# [oops I'm the pyuwsgi maintainer now (intermediate)](https://youtu.be/WILYaDNez4g)

today I take you down a rabbit hole of deadlocks and worker reloads and python 3.12 sadness.  unfortunately despite the "conclusion" in this video this doesn't actually fix the problem -- more on that in the future!

## Interactive examples

### Python

```python
import pyuwsgi
```

### Bash

Session 1:

```bash
virtualenv venv -ppython3.11
. venv/bin/activate
pip install pyuwsgi

ls venv/lib/python3.11/site-packages/
python

chmod +x t.sh
bash t.sh
kill -9 %1

pip freeze | grep pyuwsgi
deactivate

virtualenv venv -ppython3.12
. venv/bin/activate
pip install pyuwsgi

bash t.sh
```

Session 2:

```bash
yes | head -100 | xargs -P4 --replace curl localhost:9001/health-check/; echo
yes | head -1000 | xargs -P4 --replace curl localhost:9001/health-check/; echo
yes | head -1000 | xargs -P40 --replace curl localhost:9001/health-check/; echo
```
