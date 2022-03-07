# [python code formatter tutorial (intermediate - advanced)](https://youtu.be/G1omxo5pphw)

Today I show an end-to-end example of writing a code formatter similar to the ones I've written (pyupgrade / add-trailing-comma / future-fstrings / etc.)!

## Interactive examples

### Python

```python
import ast
ast.arg
```

### Bash

```bash
virtualenv venv
. venv/bin/activate
pip install tokenize-rt
pip install astpretty

astpretty --no-show-offsets target.py
astpretty target.py
tokenize-rt target.py

python t.py target.py
astpretty /dev/stdin <<< 'def f(x): pass'

python -m pydoc tokenize-rt

cp target.py backup.py
python t.py target.py

python -m pdb t.py target.py

python t.py target.py
diff -u backup.py target.py
```
