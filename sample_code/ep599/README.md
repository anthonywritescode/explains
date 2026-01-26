# [python t-strings (PEP 750)](https://youtu.be/_QYAoNCK574)

today we look at the brand new syntax coming to python 3.14, some practical applications, the good, the bad, and my thoughts.

## Setup commands

```bash
podman run --rm -it ubuntu:noble bash
apt update
apt install software-properties-common
```

## Interactive examples

### Python

```python
t'hello hello'

import string.templatelib

string.templatelib
dir(string.templatelib)

t'hello hello'
thing = 1; t'hello hello {thing}'

thing = 'world'
t'hello hello {thing}'
t'hello hello {thing!r}'

thing = 'world'
hello = f'{thing!a}'
print(hello)

thing = '☃🙃'
f'{thing!a}'
print(f'{thing!a}')

f'{thing}'
f'{thing!r}'
repr(thing)

thing = 'world'
print(f'hello {thing=}')
t'hello {thing=}'

width = 10
print(f'hello {thing:>{width}}')

width = 20
print(f'hello {thing:>{width}}')

t'hello {thing:>{width}}'
t'hello {t'hello {f'thing'}'}'

from string.templatelib import Template
import string

string.Template
Template

'hello %s' % ('world', )
'hello {}'.format('world')
f'hello {'world'}'
t'hello {'world'}'
string.Template('hello $world').substitute(world='world')

f = string.Formatter()
dir(f)
list(f.parse('hello {world}'))
list(f.parse('hello {world} ! {other} {thing}'))
list(f.parse('hello {world} ! {other!r} {thing!r}'))
```

### JavaScript

```javascript
thing = 'world'
`hello hello ${thing}`

function f(strings, arg1, arg2) {
    console.log(strings, arg1, arg2)
}

f`hello hello ${thing} !`
```

### SQLite

```sql
.schema
select * from repos;
```

### Bash

Session 1:

```bash
add-apt-repository ppa:deadsnakes/nightly
apt install python3.14
python3.14
```

Session 2:

```bash
node
cp ~/.cache/pre-commit/db.db .
sqlite3 db.db
```
