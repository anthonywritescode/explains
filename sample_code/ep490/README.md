# [RegCPython: a 10% faster python for free? (intermediate - advanced)](https://youtu.be/MQ2Lfj2hAdk)

Sounds too good to be true -- but Betteridge is wrong here!  I show how a research group produced an api and abi compatible cpython with significant speedups to pure python execution!

## Interactive examples

### Python

```python
import dis

def f(x, y, z):
    return x + y + z

dis.dis(f)
```

### Bash

```bash
python

git -C <directory> remote -v

./venv-cpython/bin/pyperformance compare results-cpython results-regcpython
```
