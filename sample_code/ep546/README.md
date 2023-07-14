# [python's "soft" keywords (intermediate)](https://youtu.be/Rv3NYDOLpkM)

Today we talk about "soft" keywords and how they allow a growing programming language to evolve without breaking the world!

## Interactive examples

### Python

```python
import re

REG = re.compile('f+')
match = REG.match('ffffffff')
match

match 1:
    case 0: print('it is zero')
    case 1: print('got one')

match 1:
    case _: print(2)

import keyword
keyword.softkwlist

type
```

### Bash

```bash
docker run -v $PWD:/src:ro --rm -ti python:3.6-slim bash

python3.6 /src/t.py
cat /src/t.py
exit

python3.7 t.py
python3.10
python3.11
python3.12
```
