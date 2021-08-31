# [virtualenv vs. venv (beginner - intermediate)](https://youtu.be/MGTX5qI2Jts)

Today I explain the basics of virtualenv / venv and why you should use them!  I also compare / contrast venv and why I tend to pick virtualenv

## Interactive examples

### Bash

Session 1:

```bash
dpkg -l | grep python3

time virtualenv venv1
source venv1/bin/activate
echo $VIRTUAL_ENV
echo $PATH
which python
which python3
pip install pre-commit
ls venv1/lib/python*/site-packages/
virtualenv venv39 -p python3.9
```

Session 2:

```bash
time python -m venv venv2
which python
which python3
. venv2/bin/activate
dpkg -l | grep -- -venv
python -m venv --help
```

### Windows CMD

```batch
python -m venv venv2
venv2\Scripts\activate
echo %PATH%
```
