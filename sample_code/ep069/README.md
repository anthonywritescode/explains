# [customizing the python repl (intermediate)](https://youtu.be/vwu6i0ghwJU)

Today I show a few ways to customize the python REPL (including fixing the annoying behaviour of exit!)

## Interactive examples

### Python

```python
exit
type(exit)
repr(exit)
type(exit).__repr__
type(exit).__repr__ = lambda self: self()
exit

pp({1: 2, 3: 4})
```

### Bash

```bash
PYTHONSTARTUP=startup.py python
```

### PowerShell

```powershell
$env:PYTHONSTARTUP = 'startup.py'
python
```
