# [refcount ONE BILLION? (immortal objects, PEP 683) (advanced)](https://youtu.be/i5ZaVC4sEZA)

A continuation to our "maybe CoW can actually work in python" series we talk about immortal objects -- and how they (accidentally?) made it into python 3.11

## Interactive examples

### Bash

```bash
python -c 'import sys; print(sys.getrefcount(0))'
python -c 'import sys; print(sys.getrefcount(None))'

python3.11 -c 'import sys; print(sys.getrefcount(None))'
python3.11 -c 'import sys; print(sys.getrefcount(0))'
python3.11 -c 'import sys; print(sys.getrefcount(b""))'
python3.11 -c 'import sys; print(sys.getrefcount(b"a"))'
python3.11 -c 'import sys; print(sys.getrefcount("a"))'
python3.11 -c 'import sys; print(sys.getrefcount(""))'
python3.11 -c 'import sys; print(sys.getrefcount("ab"))'
python3.11 -c 'import sys; print(sys.getrefcount(1))'
python3.11 -c 'import sys; print(sys.getrefcount(256))'
```
