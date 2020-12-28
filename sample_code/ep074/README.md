# [python packaging: optional dependencies (intermediate)](https://youtu.be/yJyo-K7wW2g)

Today I talk about how to declare optional dependencies in the packages you're providing as well as how to install optional dependencies in other packages!

## Interactive examples

### Bash

```bash
virtualenv venv
. venv/bin/activate
pip install .
pip freeze

pip uninstall -y foo >& /dev/null; pip install .

pip uninstall -y foo >& /dev/null; pip install .[flask]
pip uninstall -y foo >& /dev/null; pip install .[testing]
pip uninstall -y foo >& /dev/null; pip install .[testing,flask]
pip install pytest[testing]

pip install setup-py-upgrade
setup-py-upgrade .
```
