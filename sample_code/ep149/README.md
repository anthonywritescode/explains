# [python: more advanced breakpoint() usage (intermediate)](https://youtu.be/7TuFty4_WTY)

Today I talk about more advanced usage of breakpoint() such as (1) customizing the hook (2) disabling it entirely and (3) using it for difficult-to-debug scenarios like curses!

## Setup commands

```bash
git clone git@github.com:asottile/babi
# git clone https://github.com/asottile/babi
cd babi
```

## Interactive examples

### Python debugger (pdb)

```
where
q

self.perf
ret = self._get_char()
n
p ret
q
```

### Bash

```bash
python t.py
PYTHONBREAKPOINT=0 python t.py

PYTHONBREAKPOINT= python t.py
PYTHONBREAKPOINT=asdf python t.py

virtualenv venv
. venv/bin/activate
pip install pudb
PYTHONBREAKPOINT=pudb.set_trace python t.py

pip install remote-pdb
./testing/debug-babi
./testing/debug-attach
```
