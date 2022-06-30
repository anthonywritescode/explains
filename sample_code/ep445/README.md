# [argparse: boolean option pitfall (beginner - intermediate)](https://youtu.be/KuwR0GPylqE)

Today I show how to properly handle boolean options in argparse as well as an easy mistake to avoid!

## Interactive examples

### Python

```python
bool('asdfasdf')
bool('')
bool('false')
bool('False')
```

### Bash

```bash
python t.py
python t.py --help

python t.py --flag=true
python t.py --flag=false
python t.py --flag=False
python t.py --flag=

python t.py
python t.py --do-thing
python t.py --do-thing --no-do-thing

python t.py --flag=asdfasdf
python t.py --flag=True
python t.py --flag=TrUE
```
