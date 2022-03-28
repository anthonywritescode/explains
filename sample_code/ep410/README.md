# [getting a python stacktrace from gdb! (intermediate - advanced)](https://youtu.be/guni3oUdTIs)

Today I show how to attach to a python process using gdb and extract a python stacktrace for some really low level debugging!

## Interactive examples

### Bash

Session 1:

```bash
virtualenv venv
. venv/bin/activate
pip install coverage

python t.py
coverage run -m t
```

Session 2:

```bash
ps -ef | grep coverage
pstree -halp <process_id>

sudo strace -p <process_id>
sudo strace -p <another_process_id>

gdb venv/bin/python -p <process_id>
sudo gdb venv/bin/python -p <process_id>

# bt
# q

sudo apt install python<version>-dbg
dpkg -L python<version>-dbg

sudo gdb venv/bin/python -p <process_id>

# py-bt
# py-up
# py-down
# py-locals
```
