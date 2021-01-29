# [how do editable pip installs work? (intermediate)](https://youtu.be/gYYi7varbmE)

Today I talk about `pip install -e .` and how that makes a library live-editable!

## Setup commands

```bash
git clone git@github.com:asottile/astpretty
# git clone https://github.com/asottile/astpretty
cd astpretty
```

## Interactive examples

### Bash

```bash
virtualenv venv
. venv/bin/activate
pip install --editable .
astpretty t.py

nano astpretty.py
astpretty t.py

pip uninstall astpretty
pip install .

nano astpretty.py
astpretty t.py

deactivate
git clean -fxfd

virtualenv venve
. venve/bin/activate
pip install --editable . -vvv --disable-pip-version-check
ls astpretty.egg-info
nano venve/lib/python3.8/site-packages/easy-install.pth
```
