# [python warnings (beginner - intermediate) explains #320](https://youtu.be/tZSEZ2WG5w8)

Today I talk about the warnings module and the argument you *absolutely* need whenever you raise a warning (as well as how to turn them into errors and/or silence them!)

## Interactive examples

### Python

```python
Warning
Warning.__subclasses__()

from pprint import pprint as pp
pp(Warning.__subclasses__())
```

### Bash

```bash
python -m pydoc warnings
python -m app
python -W error -m app
PYTHONWARNINGS=error python -m app
PYTHONWARNINGS=once python -m app
PYTHONWARNINGS=always python -m app
PYTHONWARNINGS=ignore::SyntaxWarning python -m app
PYTHONWARNINGS=ignore:foo python -m app
```
