# [debugging python segfaults with gdb (intermediate - advanced)](https://youtu.be/bXEXE6ywzSA)

Occasionally something goes wrong in C code and you need to drop into gdb to debug it!  here's a quick tutorial for showing how to do that, and how to use the debug builds of python!

## Interactive examples

### Python

```python
import sample_c_extension
sample_c_extension.hello_world()
```

### Bash

```bash
virtualenv venv
. venv/bin/activate
pip install .

python -c 'import sample_c_extension; sample_c_extension.hello_world()'
ls
cat /proc/sys/kernel/core_pattern

ulimit -c unlimited
python -c 'import sample_c_extension; sample_c_extension.hello_world()'
ls
gdb python core
# bt
# q

python t.py
gdb python
# run
# run t.py
# p ptr
# q

pip install pytest
gdb python
# run -m pytest test.py
# q

sudo apt install python3-dbg
deactivate

virtualenv venv-dbg -p python3-dbg
. venv-dbg/bin/activate
pip install .

gdb python
# run -m t
# bt
```
