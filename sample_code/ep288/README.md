# [flake8: avoiding F401 in \_\_init\_\_.py (beginner - intermediate)](https://youtu.be/OAqvLDRZqFc)

Today I show an easy way to fix the F401 error code from pyflakes+flake8!

## Interactive examples

### Python

```python
import mypkg
mypkg.some_function()

from mypkg import *
x

import mypkg
mypkg.x
```

### Bash

```bash
python
flake8 mypkg/
```
