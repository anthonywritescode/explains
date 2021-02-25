# [what is a pager / less ? (beginner - intermediate)](https://youtu.be/hxvAEr9Q2A4)

Today we talk about what a pager is as well as the few common operations I use a pager for!

## Setup commands

```bash
virtualenv venv

. venv/bin/activate
pip install pytest

git clone git@github.com:pre-commit/pre-commit
# git clone https://github.com/pre-commit/pre-commit
```

## Interactive examples

### Bash

```bash
git log
pytest t.py | less
pytest t.py --color=yes | less
pytest t.py | less -R
```
