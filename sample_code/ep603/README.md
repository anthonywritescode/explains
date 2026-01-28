# [python 3.14 gets tail call (it's not what you think)](https://youtu.be/WlJGa_qzvA4)

today we explain "tail call optimization" and the new "tail calling interpreter" in python 3.14 and why it's mostly a nothingburger :/

## Interactive examples

### Bash

```bash
python3 -m dis t.py

cd cpython/
git grep switch -- Python/
```
