# [virtualenv: --system-site-packages (intermediate)](https://youtu.be/R6ObMPdixj0)

Today I talk about the --system-site-packages argument to venv / virtualenv and what it does and why you probably shouldn't use it (but also some tips if you do need it!)

## Interactive examples

### Python

```python
import click
click.__file__
```

### Bash

Session 1:

```bash
python -m venv venv --system-site-packages
. venv/bin/activate
pip freeze

pip install astpretty
pip freeze
pip freeze -l
# pip freeze --local

pip install pytz
pip install pytz --upgrade
pip freeze
pip freeze -l
```

Session 2:

```bash
python -m venv venv_normal
. venv_normal/bin/activate
pip freeze
```
