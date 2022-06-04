# [python: raw (NOT REGEX) r'strings' (beginner - intermediate)](https://youtu.be/RvoKwGekk1s)

Today I talk about raw strings, invalid escape sequences (W605), and how to automatically fix them!

## Interactive examples

### Python

```python
r'foo'
R'foo'
r'foo' == 'foo'

'foo\nbar'
print('foo\nbar')
print(r'foo\nbar')
r'\'
r'\'foo'
print(r'\'foo')

'\\'
print('\\')

thing = 1
print(fr'foo\n{thing}')

'\d+'
'\u2603'

r'\d+'
```

### Bash

```bash
python -Wonce

virtualenv venv
. venv/bin/activate
pip install flake8
flake8 t.py

pip install pyupgrade
python -Werror t.py
pyupgrade t.py
```
