# [cd is not an executable (beginner)](https://youtu.be/1Ld5qv4-Pbo)

Today I show an easy beginner mistake -- `cd` isn't actually an executable!

## Interactive examples

### Python

```python
import os
os.getcwd()

# Ctrl-z
os.chdir('/home')
```

### Bash

```bash
python t.py

type cd

cd /tmp
# mkdir explains

python
# Ctrl-z

cd explains/
fg
pwd

sh -c 'cd astpretty'
pwd

bash -x t.sh
echo $?

source t.sh
pwd
```
