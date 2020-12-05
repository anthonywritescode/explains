# [implementing --version with importlib.metadata (intermediate)](https://youtu.be/beDG6Ibo2zQ)

Today I show how to implement an argparse --version option using importlib.metadata (new in python 3.8) as well as how to use the backported version for older pythons!

## Setup commands

```bash
git clone git@github.com:asottile/astpretty

tox --devenv venv

. venv/bin/activate
```

## Interactive examples

### Python

```python
import importlib.metadata
importlib.metadata.version('astpretty')
importlib.metadata.version('asdfasdf')

# python3.7
import importlib_metadata
importlib_metadata.version('astpretty')
```

### Bash

```bash
astpretty t.py
astpretty --version
python -m pydoc argparse
python -V
python --version
python astpretty.py --version
python -m astpretty --version
tox --devenv venv37 -e py37
. venv37/bin/activate
```
