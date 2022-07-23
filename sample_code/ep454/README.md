# [javascript sucks at unicode (intermediate)](https://youtu.be/PTJAvcpBdWo)

Today we go over an annoying javascript quirk related to unicode -- surprise surprise python fixed this years ago!

## Interactive examples

### Node

```javascript
s = '🙃'
s.length

s[0]
s[1]

console.log(s[1])

for (let char of s) {
    console.log({char})
}

s += ' hello hello'

for (let char of s) {
    console.log({char})
}

[...s].length
s.length

s.slice(1)
[...s].slice(1).join('')
```

### Python

```python
len('🙃')

import unicodedata
unicodedata.name('\ud83d')
```

### Bash

```bash
python -m http.server
node
```
