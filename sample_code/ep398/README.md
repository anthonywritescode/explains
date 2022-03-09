# [from imports aren't faster! (beginner - intermediate)](https://youtu.be/ZWCyNz0fUsc)

I often hear the assertion that python from imports are faster because they don't need to import the whole module (or that they save memory, etc. etc.) -- I show why that's wrong and how the import system works!

## Interactive examples

### Python

```python
import sys
sys.modules['cs50']

sys.path

from cs50 import get_int
sys.module['cs50']
dir(sys.module['cs50'])

get_int
sys.modules['cs50'].get_int
```

### Bash

```bash
virtualenv venv
. venv/bin/activate
pip install cs50

python
```
