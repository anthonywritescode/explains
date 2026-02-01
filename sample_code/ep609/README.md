# [calling open breaks this module?](https://youtu.be/qfv83iTplfw)

today we take a look at one of the more surprising python 2 behaviours and a fun little bug I ran into when working at a previous company

## Interactive examples

### Python

```python
import string
string.ascii_letters

import random
random.sample(string.ascii_letters, 3)

random.seed(123)
''.join(random.sample(string.ascii_letters, 12))

random.seed(123); ''.join(random.sample(string.ascii_letters, 12))
random.seed(123); ''.join(random.sample(string.ascii_letters, 12))
random.seed(123); ''.join(random.sample(string.ascii_letters, 12))

contents = open('f').read()
type(contents)
str is bytes

import io
io.open('f').read()
type(io.open('f').read())

import string
string.ascii_letters

import string
import io

io.open('/dev/null').close()
string.ascii_letters

import string
string.letters

import string
import io

io.open('/dev/null').close()
string.letters

import string
string.letters

import locale
dir(locale)

locale.getpreferredencoding()
string.letters
```

### Bash

```bash
python3 -m pydoc string
python3

docker run --rm -ti python:2.7-slim bash

echo hello hello > f
python

python3 -m pydoc io
```
