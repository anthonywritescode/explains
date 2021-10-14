# [range(len(...)) is almost always wrong in python (beginner)](https://youtu.be/SwjBJhJiHvQ)

Today I talk about a common pattern I see in beginner python and a trick or two to avoid it!

## Interactive examples

### Python

```python
list(enumerate((1, 2, 3)))
list(enumerate(('a', 'b', 'c')))
list(enumerate(('a', 'b', 'c'), start=1))
```

### Bash

```bash
python t.py
python -m pydoc enumerate
python -m pydoc itertools.islice
```
