# [hacker mode tmux debugging (intermediate)](https://youtu.be/BMn0nSpeITY)

Today I give a quick introduction to tmux and then show one of the coolest debugging techniques I've come up with which uses tmux!

## Interactive examples

### Bash

```bash
tmux
# create tab: Ctrl-b + c
# switch to tab 0: Ctrb-b + 0
# detach from tmux: Ctrl-b + d
tmux attach
# exit tab: Ctrl-d
python2 t.py
# python t.py
python3 t.py
# split into panes: Ctrl-b + %
# switch panes: Ctrl-b + <arrow_keys>
# tmux command prompt: Ctrl-b + :
# synchronize command: setw synchronize-panes
```
