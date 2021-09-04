# [Fussy Fox + flake8 vulnerability (intermediate)](https://youtu.be/J7NMyb-LNX4)

Today I talk about a vulnerability in the Fussy Fox linting service which I disclosed and got permission to post about.

## Interactive examples

### Bash

```bash
virtualenv venv
. venv/bin/activate

pip install flake8
flake8 t.py

pip install flake8-typing-imports
flake8 t.py
```
