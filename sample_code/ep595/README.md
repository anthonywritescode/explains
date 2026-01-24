# [python now has dict unpacking?](https://youtu.be/eqiM0xRmFJg)

and it has had it since python 3.10 ???

## Interactive examples

### Python

```python
[a, b] = [1, 2]
a
b

dct = {'a': 1, 'b': 2}
{a, b} = dct
```

### JavaScript

```javascript
let obj = {'hello': 'world', other: [2, 3, 4]}
const {hello, other: [first, ...rest]} = obj

hello
first
rest
```

### Bash

Session 1:

```bash
python3
node

python3 t.py

virtualenv venv
. venv/bin/activate
pip install dict-unpacking-at-home

python3 --version
deactivate
rm -rf venv/

virtualenv venv -ppython3.10
. venv/bin/activate
pip install dict-unpacking-at-home

python3 --version
python3 t.py

dict-unpacking-at-home-show t.py
python3 t.py
```

Session 2:

```bash
podman run --rm -ti python:2.7 bash

python --version
nano t.py
python t.py

pip install future-fstrings
nano t.py
python t.py
```
