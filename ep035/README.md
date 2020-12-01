# [python single vs double quote strings! (beginner)](https://youtu.be/TTo5LGXYsH0)

Today I talk about the differences between single quote and double quote strings and some advice on which to choose -- also featuring pre-commit-hooks and black!

## Setup commands

```bash
virtualenv venv

. venv/bin/activate

pip install black

pip install pre-commit-hooks
```

## Interactive examples

### Python

```python
'foo' == "foo"
'hello " world'
"hello \" world"
```

### Bash

```bash
black t.py
cat t.py
double-quote-string-fixer t.py
cat t.py
black --help
# black --skip-string-normalization t.py
# black -S t.py
```
