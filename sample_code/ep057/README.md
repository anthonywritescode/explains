# [python packaging: basic setup.py and declarative metadata (intermediate)](https://youtu.be/GaWs-LenLYE)

Today I go over a basic setup.py for packaging a python package.  I then show a few tools you can use to migrate from classic setup.py to more easily rewritable setup.cfg!

## Interactive examples

### Python

```python
import setuptools
setuptools.find_packages()
setuptools.find_packages(exclude=('tests*', 'testing*'))
```

### Bash

```bash
mkdir hello_world
touch !$/__init__.py
nano hello_world/main.py

tree .

mkdir tests
touch tests/test_foo.py
touch tests/__init__.py

mkdir testing
touch testing/helper.py
touch testing/__init__.py

virtualenv venv
. venv/bin/activate

pip install .
pip freeze

hello-world-cli

pip install setup-py-upgrade
setup-py-upgrade .

pip install setup-cfg-fmt
setup-cfg-fmt setup.cfg
```
