# [what's that unicode character‽ (beginner - intermediate)](https://youtu.be/W60RS8PMP78)

Today I show a little python trick for figuring out a particular unicode character!

## Interactive examples

### Python

```python
import unicodedata

unicodedata.name('a')

s = "🇺🇸"
for c in s:
    print(unicodedata.name(c))

for c in s:
    print(unicodedata.name(c), ord(c))

for c in s:
    print(unicodedata.name(c), hex(ord(c)))

print('\U0001f1fa')
print('\U0001f1f8')
```

### Bash

```bash
python
```
