# [what is atomicity (intermediate)](https://youtu.be/tmlmCG5egI0)

Today I talk about what atomicity is in software and also show an example of a non-atomic operation and a technique to make it atomic

## Interactive examples

### Bash

Session 1:

```bash
python -m pydoc threading
watch -n.1 cat foo
tmux

# tmux session 1
watch -n.1 cat foo

# tmux session 2
watch -n.1 cat foo.tmp
```

Session 2:

```bash
python t.py
```
