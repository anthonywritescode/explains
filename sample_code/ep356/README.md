# [python: unicode names and why they're bad (intermediate)](https://youtu.be/OaEgGW19M5o)

Today I talk about unicode variable names in python and why they're potentially problematic!

## Interactive examples

### Python

```python
a = 1
π = 3.1415926535
π

print('\u2603')
☃ = 'snowman'

A = 4
Α = 5
print(A)

import unicodedata
unicodedata.name('A')
unicodedata.name('Α')
```

### Bash

```bash
# python
python3
```
