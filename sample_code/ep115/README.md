# [python typing: re.match and Optional (intermediate)](https://youtu.be/yH6L3UiK9WM)

Today I talk about Optional and a few approaches to typing the return value of `re.match` (which returns an `Optional[Match[str]]`)!

## Interactive examples

### Bash

```bash
virtualenv venv
. venv/bin/activate
pip install mypy

mypy t.py
python t.py
```
