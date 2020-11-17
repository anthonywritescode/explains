# [python's tricky `for ...: else:` statement (beginner - intermediate)](https://youtu.be/8P7lXLXR_3c)

Today I explain one of my favorite syntax features from python, the `for ...: else:` statement! (as well as `while ...: else:`, but that one's kinda rare).

I also show a few real-world examples from my code at the end!

## Interactive examples

### Python

```python
str_find_char('hello', 'o')
str_find_char('hello', 'z')
```

### Bash

```bash
python -i t.py

# source code for all-repos-find-files: https://github.com/asottile/all-repos
all-repos-find-files --outputh-paths '\.py$' | xargs python t.py | grep -E 'asottile|anthonywritescode|pre-commit'
```
