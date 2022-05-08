# ["z3" is actual magic (intermediate)](https://youtu.be/C9eXcmWWEyA)

Today I show off "z3" -- the coolest software tool I've ever used which can magically solve problems just by knowing the problem description

## Interactive examples

### Python

```python
import z3
opt = z3.Optimize()
opt.add(z3.Int('x') > 5)
opt.minimize(z3.Int('x'))
opt.check()
opt.model()

ord('a')
ord('z')
```

### Bash

```bash
head -c 100 pokemon.js
node pokesona.js

virtualenv venv
. venv/bin/activate
pip install z3-solver

python t.py
```
