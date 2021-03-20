# [showing actual file bytes with hexdump (beginner - intermediate)](https://youtu.be/FNyo1CSxBrg)

Today I show a useful commandline utility to show the actual contents of a file.  This can be particularly useful when looking at escape sequences or trying to see invisible characters

## Setup commands

```bash
git clone git@github.com:pre-commit/pre-commit
# git clone https://github.com/pre-commit/pre-commit

cd pre-commit
```

## Interactive examples

### Python

```python
0o033
hex(0o033)
print('\x1b[42mhello\x1b[m')
```

### Bash

```bash
man hexdump
dpkg -S $(which hexdump)

pre-commit run flake8 --all-files
pre-commit run flake8 --color=always
pre-commit run flake8 --color=always | hexdump
pre-commit run flake8 --color=always | hexdump -C
pre-commit run flake8 --color=always | hd
pre-commit run flake8 --color=always | hd -c
hd -c /bin/echo
strings /bin/echo
```
