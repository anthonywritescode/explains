# [python warnings defaults suck (intermediate)](https://youtu.be/CtFdXBEwYfk)

Today I talk about an extremely common mistake with python warnings -- and what I wish the default behaviour was

## Interactive examples

### Bash

```bash
python -m t
PYTHONWARNINGS=once python -m t

python -Wonce -m t
python -Werror -m t
```
