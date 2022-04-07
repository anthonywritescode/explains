# [bash protip: fc "fix command" (beginner - intermediate)](https://youtu.be/PPovOOA7bdU)

Today I talk about a neat little tip that lets you edit the previous command (and current command) in your shell with a text editor!

## Interactive examples

### Bash

```bash
babbi t.py
fc
echo $VISUAL
echo $EDITOR
unset VISUAL
unset EDITOR
fc

pytest part1.py && python part1.py
# Ctrl-x-e
```
