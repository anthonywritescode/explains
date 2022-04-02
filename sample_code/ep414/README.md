# [`pip install pkg❮1.999` ? (intermediate)](https://youtu.be/JzEAYIPdFX4)

Today I show an oddity of a requirements file due to an old behaviour of pip (and a rather surprising behaviour of `packaging`!)

## Interactive examples

### Python

```python
from packaging.version import Version

v1 = Version('0.15.0')
v2 = Version('0.16.0')

v1 <= Version('0.15.0') < Version('0.16.0')
v1 <= Version('0.15.1') < Version('0.16.0')
v1 <= Version('0.16.0') < Version('0.16.0')

Version('0.15.0') <= Version('0.16.0a') < Version('0.16.0')
Version('0.15.0') <= Version('0.16.0a1') < Version('0.16.0')
```

### Bash

Session 1:

```bash
# git clone https://github.com/asottile/cheetah_lint
git clone git@github.com:asottile/cheetah_lint
cd cheetah_lint/

nano setup.cfg
cd ..

virtualenv venv
. venv/bin/activate
pip install packaging

python

pip install pypiserver
pypi-server y/dist
```

Session 2:

```bash
mkdir y
cd !$
touch wat.py

virtualenv venv -ppython3.5
. venv/bin/activate
python setup.py bdist_wheel

ls dist/
pip install 'pip<6'
pip install --pre 'wat>=1,<2' --index-url http://localhost:8080/simple
pip uninstall -y wat

pip install pip'<7' --upgrade
pip install --pre 'wat>=1,<2' --index-url http://localhost:8080/simple
```
