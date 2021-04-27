# [python typing: object vs Any (intermediate)](https://youtu.be/ATS9MAo2Mjc)

Today I talk about the difference between object and Any when typing things!

## Interactive examples

### Python

```python
C(1) == 1
C(1) == C(1)
C(1) == C(2)
```

### Bash

```bash
virtualenv venv
. venv/bin/activate
pip install mypy

mypy t.py
python -m t.py
```
