# [python: raising Error without parens (intermediate)](https://youtu.be/gGqRBHHIQGE)

Today I explain a minor nuance in raising exceptions and some advice on picking the _slightly_ faster alternative :)

## Interactive examples

### Python

```python
import dis
dis.dis(f)
dis.dis(g)


import timeit
timeit.timeit(f)
timeit.timeit(g)
```

### Bash

```bash
python -i t.py
```
