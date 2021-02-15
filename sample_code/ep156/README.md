# [python regex: \\d gotcha! (beginner - intermediate)](https://youtu.be/9dnZiCW1OHc)

\d matches numbers right? welllllllllll maybe not the numbers you expected!

## Interactive examples

### Python

```python
import re

reg = re.compile(r'\d+')
reg.match('123123')
reg.match('٣٤٥')

import unicodedata
unicodedata.name('٣')

reg = re.compile(r'\d+', re.ASCII)
reg.match('٣٤٥')
reg.match('123123')

reg = re.compile(r'[0-9]+')
reg.match('123123')
reg.match('٣٤٥')
```

### Bash

```bash
python t.py
```
