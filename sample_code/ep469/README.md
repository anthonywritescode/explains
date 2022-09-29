# [why can't I signal a MagicMock() ? (intermediate)](https://youtu.be/nJwc7iqyQwU)

Today I show how I debugged a stackoverflow question about signaling a MagicMock (as well as how to fix it!)

## Interactive examples

### Python

```python
from unittest import mock
m = mock.Mock()
m()
```

### Python debugger (pdb)

```
s
s
_signal
_enum_to_int(handler)
handler
handler.__int__
handler.__int__()
```

### Bash

```bash
python t.py

kill -l
```
