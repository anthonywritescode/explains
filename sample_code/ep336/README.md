# [porting code to python **ZERO** (intermediate - advanced)](https://youtu.be/6vdg91-hPGY)

Today we do a bit of time travelling to look at the very first release of python!  it's surprisingly similar and actually not too difficult to write a single-source script which works in every version from python 0.9.1 to python 3.11!

## Setup commands

```bash
git clone git@github.com:asottile/ancient-pythons
# git clone https://github.com/asottile/ancient-pythons
cd ancient-pythons
```

## Interactive examples

### Python

```python
import path

'foo'
"foo"

dir(path)
path.cat('foo', 'bar')

import dis
dis.dis()

x = 1
if x = 2:
    print('got 2')

if x = 1:
    print('got 1')

if x <> 1:
    print('got not 1')

if 'f' = 'f':
    print('equal')

if 'ff' = 'ff':
    print('equal')

range(1)

x = {}
x['a'] = 1
x['b'] = 2
x
```

### Bash

```bash
# git clean -fxfd
./make0x.py python-0.9.1
./bin/python0.9.1
```
