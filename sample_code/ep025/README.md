# [a flake8 plugin from scratch (intermediate)](https://youtu.be/ot5Z4KQPBL8)

Today I build a flake8 plugin from scratch showing the bare minimum to add a new lint check!  I also demo all the related tools I use to make this happen: astpretty, pytest, flake8, and a little bit of python packaging!

## Setup commands

```bash
virtualenv venv

. venv/bin/activate

pip install flake8 pytest astpretty
```

## Interactive examples

### Python

```python
import importlib.metadata
importlib.metadata.version('flake8_named_arguments')

'foo'.isidentifier()
'foo-bar'.isidentifier()
```

### Bash

```bash
pip install -e .
flake8 --help
pytest tests
astpretty /dev/stdin <<< "f(**{'foo': 'bar'})"
astpretty --no-show-offsets /dev/stdin <<< "f(**{'foo': 'bar'})"
astpretty --no /dev/stdin <<< "f(**{'foo': 'bar'})"
```
