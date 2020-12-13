# [python \_\_future\_\_ "module" (beginner - intermediate)](https://youtu.be/_K4mjPrROGQ)

Today I talk about the __future__ module (not to be confused with the future module!) and how it affects execution in python.

## Interactive examples

### Python

```python
# python2
2 / 3

# python3
2 / 3
2 // 3

# python2
from __future__ import division

2 / 3

type('')

from __future__ import unicode_literals

type('')

# python3
5 <> 4

from __future__ import barry_as_FLUFL

5 <> 4

__doc__
```

### Bash

```bash
python t.py

python -m pydoc __future__

python -i t.py
```
