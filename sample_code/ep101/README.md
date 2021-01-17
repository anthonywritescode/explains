# [namedtuple to json and other pitfalls (intermediate)](https://youtu.be/QOKqvuvA3ok)

Today we continue talking about namedtuples -- today how to convert them to json and the pitfalls of being a tuple.

## Interactive examples

### Python

```python
import json
user = User(name='Anthony', age=29, location='CA')
json.dumps(user)
print(json.dumps(user))
print(json.dumps(('Anthony', 29, 'CA')))
user._asdict()
print(json.dumps(user._asdict(), indent=2))
user._fields
user._field_types  # user.__annotations__
user._field_defaults
```

### Bash

```bash
python -i t.py
```
