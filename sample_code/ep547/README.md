# [shell vs environment variables (and env, export, etc.) (intermediate)](https://youtu.be/h36Xc38SDHg)

Today we talk about environment variables, shell variables, shorthand(s) for setting them and unsetting them!

## Interactive examples

### Python

```python
import os
'X' in os.environ
```

### Bash

```bash
NOSHOW=1 python3 -um scripts.swsh.da --pokemon da-targets --quiet

X=1
echo "$X"

python3

bash -c 'echo $X'
echo $X

export X
bash -c 'echo $X'

export X=2
bash -c 'echo $X'

export -n X
bash -c 'echo $X'

unset X
echo $X

X=1 bash -c 'echo $X'
echo $X

X=1 Y=1 Z= bash -c 'echo $X $Y $Z'

man test

which env

env X=1 bash -c 'echo $X'
env X=1 Y=1 bash -c 'echo $X $Y'

env bash -c 'echo $USER'
env -i bash -c 'echo $USER'
```
