# [am I vulnerable to black's CVE? (2024-21503) (intermediate)](https://youtu.be/2P20wZGsdJQ)

today we walk through an analysis of black's recent CVE regarding regular expressions and whitespace!  It's marked "Medium" with "Network" attack vector and we'll show whether it matters or not!

## Interactive examples

### Python

```python
import re

reg = re.compile(r"\s*\t+\s*(\S)")
reg.match('    \t\t\t\t\t    \t1')
reg.match('    \t\          ')
reg.match('    \t          ')

reg.match('\t' * 25)
reg.match('\t' * 50)
reg.match('\t' * 100)
reg.match('\t' * 200)
reg.match('\t' * 300)
reg.match('\t' * 400)
reg.match('\t' * 500)
reg.match('\t' * 600)

reg = re.compile(r"(\s)(\S)")
reg.match('\t' * 600)

with open('t.py', 'w') as f:
    f.write('"""\n')
    f.write('\t' * 500 + '\n')
    f.write('"""\n')
```

### Bash

```bash
python3

python3.11

virtualenv venv
. venv/bin/activate
pip install black
black --check t.py

pip install 'black<24.3'
rm -rf ~/.cache/black
black --check t.py
```
