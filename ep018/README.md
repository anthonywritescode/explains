# [postmortem debugging in python (beginner - intermediate)](https://youtu.be/s8Nx2frW4ps)

Today I go over one of my favorite debugging techniques and three ways to use it (scripts, inline, or with pytest!)

## Setup commands

```bash
virtualenv venv

. venv/bin/activate

pip install pytest
```

## Interactive examples

### Bash

```bash
python -m pdb t.py
pytest test.py
pytest test.py --pdb
```
