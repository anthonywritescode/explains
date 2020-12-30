# [bash hash cache! (beginner - intermediate)](https://youtu.be/N13XEwdc_2k)

Today I talk about the hash cache in bash and show how it can sometimes produce confusing / incorrect results (and how to clear it!).

## Interactive examples

### Bash

```bash
pre-commit --version
which pre-commit

virtualenv venv
. venv/bin/activate

pip install pre-commit==2.5.0
pre-commit --version

pip uninstall pre-commit
pre-commit --version

hash -l
which pre-commit

hash -r
hash -l

pre-commit --version
hash -l

deactivate
hash -l
```
