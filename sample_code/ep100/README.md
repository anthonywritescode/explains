# [intro to python namedtuples! (beginner - intermediate)](https://youtu.be/iqXnBE4htUc)

Oh hey, it's episode 100!  today I talk about one of my favorite ways to make plain-old-data classes in python!

## Interactive examples

### Python

```python
import sys
sys.version_info
sys.version_info[0]
a, b, c, *_ = sys.version_info
a
b
c

users = get_users()
users[0]
users[0].name
users[0].age
users[0].location

user = get_users()[0]
user.name = 'asdfasdf'
```

### Bash

```bash
python t.py
python -i t.py
```
