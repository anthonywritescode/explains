# [you're probably doing case-insensitive wrong (intermediate)](https://youtu.be/U-Zq8bURfKc)

Today I talk about `casefold` and the edge cases it handles that aren't handled by `.lower()`!

## Interactive examples

### Python

```python
'ß'
'ß'.upper()

'ß'.lower()
'ß'.lower() == 'ß'

'ß'.casefold()

import unicodedata

unicodedata.name('ﬀ')
'ﬀ'.lower() == 'ﬀ'

'ﬀ'.casefold()
```

### Bash

```bash
python t.py
python t.py | less
```
