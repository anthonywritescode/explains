# [why I banned python's assertRaises (intermediate)](https://youtu.be/Q_HMOBD09ts)

Today I walk through why I banned `assertRaises` in tests at work as well as an alternative that doesn't have this pitfall

## Interactive examples

### Python debugger (pdb)

```
x
y
up
x
y
q
```

### Bash

```bash
python -m unittest t

virtualenv venv
. venv/bin/activate
pip install pytest

pytest t.py
pytest t.py --pdb
```
