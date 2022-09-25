# [why can't I signal a MagicMock() ? (intermediate)](https://www.youtube.com/watch?v=nJwc7iqyQwU)

Today I show how I debugged a stackoverflow question about signaling a MagicMock (as well as how to fix it!)

## Interactive examples

### Bash

Session 1:

```bash
babi t.py
python3 t.py
```

Session 2:

```bash
kill -l
```

### Python debugger (pdb)

```
s
s
_signal
_enum_to_int(handler)
handler
handler.__int__()
q
```

### Python

```python
from unittest import mock
m = mock.Mock()
m()
```
