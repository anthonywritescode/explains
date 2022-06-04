# [regex lookahead / lookbehind (intermediate)](https://youtu.be/AjTy0DBK-18)

Today we have another regex feature to talk about: lookaheads and lookbehinds!  I show how they can be used to validate surrounding text without matching it

## Interactive examples

### Python

```python
import re

s = 'hello hello world'
reg = re.compile('hello(?= hello)')
reg.findall(s)

reg2 = re.compile('hello')
reg2.findall(s)

reg = re.compile('hello(?! hello)')
reg.search(s)

reg3 = re.compile(r'(?<!\\)(\\\\)*\\[u]')
reg3.search(r'hello \\\\\u world')
# ^ $

reg = re.compile('hello(?! hello)(?! world)(?! foo)')
reg.search('hello hello')

reg = re.compile('hello(?! hello)(?! world)(?! foo)(?!$)')
reg.search('hello hello')
reg.search('hello world')
reg.search('hello anthony')
```

### Bash

```bash
python
```
