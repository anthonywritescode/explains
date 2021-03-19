# [python: why is -c faster than -m? (intermediate)](https://youtu.be/YuIZkHawihw)

Today I answer an interesting question which surprised me -- why is `python -c ...` faster than `pyhon -m ...` (even when they do the same thing)?

## Interactive examples

### Bash

Session 1:

```bash
python -m site --user-base
time python -m site --user-base
time python -X importtime -m site --user-base
```

Session 2:

```bash
python -c 'import site; print(site.getuserbase())'
time python -c 'import site; print(site.getuserbase())'
time python -X importtime -c 'import site; print(site.getuserbase())'
time python -X importtime -c ''
time python -X importtime -S -c ''
```
