# [the `wc` command (beginner)](https://youtu.be/YmjeLv1RLSc)

Today I talk about the `wc` command and how it's much more useful for finding the size of things than opening `nano` / `vim` and looking at the footer!

## Setup commands

```bash
git clone git@github.com:pre-commit/pre-commit
# git clone https://github.com/pre-commit/pre-commit

cd pre-commit
```

## Interactive examples

### Bash

```bash
man wc
wc setup.cfg
git ls-files -- '*.py' | wc -l
git ls-files -- '*.py' | xargs wc -l
git ls-files -z -- '*.py' | wc --files0-from=-
git ls-files -z -- '*.py' | wc --files0-from=- -l
git ls-files -z -- '*.py' | wc --files0-from=- -l | sort
git ls-files -z -- '*.py' | wc --files0-from=- -l | sort -n
git ls-files -z -- '*.py' | wc --files0-from=- -l | sort -rn
```
