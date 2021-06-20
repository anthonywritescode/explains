# [python: explicit relative imports (intermediate)](https://youtu.be/uwtupH7LJco)

Today I talk about explicit relative imports in python -- how they work, what their syntax is, and why you might want to / might want to use them

## Interactive examples

### Bash

```bash
mkdir -p a/b/c
touch a/__init__.py a/b/__init__.py a/b/c/__init__.py
touch a/b/c/{foo,bar}.py
echo a/b/c/{foo,bar}.py

python -m a.b.c.foo
python a/b/c/foo.py
```
