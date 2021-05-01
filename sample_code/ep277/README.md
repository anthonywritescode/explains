# [the `find` command (beginner - intermediate)](https://youtu.be/y6NQTZgPNPw)

Today I talk about the find command (the linux one, not the windows one) and a few useful ways to use this mini-language!

## Interactive examples

### Bash

```bash
virtualenv venv
man find

find venv
find venv -print
find venv -executable
find venv -type f -executable
find venv -type f -o -executable
find venv '(' -type f -o -executable ')'

find venv -name '*.typed'
find venv -name '*.ps1'
find venv -name '*.py'
find venv -name '__init__.py'
find venv -wholename '*/pip/*/__init__.py'

./venv/bin/python -c 'import pip'
find venv -name '*.pyc' -delete
find venv -name '*.pyc'

find venv/bin -type f
find venv/bin -type f -exec python -c "import sys; print(sys.argv)" '{}' ';'
find venv/bin -type f -exec python -c "import sys; print(sys.argv)" '{}' '+'
find venv/bin -type f -print0 | xargs -0 python -c "import sys; print(sys.argv)"
```
