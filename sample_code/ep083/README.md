# [why you should end a file in a newline (beginner)](https://youtu.be/r5nWtfwK_dk)

Today I talk about why a file should end in a newline by convention and show you how to fix it!  this also covers the flake8 errors W292 and W391

## Setup commands

```bash
virtualenv venv
. venv/bin/activate
pip install flake8
```

## Interactive examples

### Bash

```bash
echo -n 'foo'
echo -n 'x = 1' > t.py
flake8 t.py

echo -en 'x = 1\n' > t.py
flake8 t.py

echo -en 'x = 1\n\n' > t.py
flake8 t.py

echo -n 'x = 1' > t.py
cat t.py
```
