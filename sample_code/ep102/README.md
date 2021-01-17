# [how namedtuple works (advanced)](https://youtu.be/sfDSQSj-uvQ)

Continuing the namedtuple vids here's one explaining the magic behind namedtuple -- we write our own version of `collections.namedtuple`!

## Interactive examples

### Python

```python
user = User('Anthony', 29, 'CA')
user
type(user)
user[0]
user[1]
user[2]

User('Anthony', 29, 'Ca')
```

### Bash

```bash
python t.py
python -i t.py
```
