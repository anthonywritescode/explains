# [how to use python backports + setup.py (intermediate)](https://youtu.be/B94tqnXeFnQ)

Today I show how to use backported libraries and how to set up your setup.py / setup.cfg to conditionally install those packages!

## Interactive examples

### Python

```python
import datetime

datetime.datetime.strptime('2022-01-01', '%Y-%m-%d')
```

### Bash

```bash
python3.9 -m tzname 2021-01-01
python3.9 -m tzname 2021-06-01

virtualenv venv -ppython3.9
. venv/bin/activate
pip install .

tzname 2021-01-01

python3 --version

virtualenv venv38 -ppython3.8
. venv38/bin/activate
pip install .
pip install backports.zoneinfo

tzname 2021-01-01
tzname 2021-06-01

deactivate
rm -rf venv38


virtualenv venv38 -ppython3.8
. venv38/bin/activate
pip install .

tzname 2021-01-01
tzname 2021-06-01

deactivate

virtualenv venv39 -ppython3.9
. venv39/bin/activate
pip install .

tzname 2021-01-01
tzname 2021-06-01
```
