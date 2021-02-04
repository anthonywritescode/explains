# [making python releases less painful with abi3 (intermediate - advanced)](https://youtu.be/4uy0c855msk)

Continuing the discussion on C extensions, I talk about abi3 and how it can make binary python distributions future proof!

## Interactive examples

### Python

```python
import _hello_world
_hello_world.hello_world()
```

### Bash

```bash
virtualenv venv -p python3.6
. venv/bin/activate
pip install .

ls venv/lib/python3.6/site-packages/_hello_world.cpython-36m-x86_64*
cp venv/lib/python3.6/site-packages/_hello_world.cpython-36m-x86_64* .
python3.6
python3.7
rm _hello_world.cpython-36m-x86_64*

pip wheel .
ls hello_world*.whl

virtualenv venv37
. venv37/bin/activate
pip install hello_world*.whl
rm *.whl


. venv/bin/activate
pip install .
ls venv/lib/python3.6/site-packages/_hello_world.*
pip wheel .
ls *.whl
rm *.whl


pip wheel .
ls hello_world*.whl
. venv37/bin/activate
pip install hello_world*.whl


. venv/bin/activate
pip install .
```
