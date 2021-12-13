# [pip: requirements vs. constraints (intermediate)](https://youtu.be/SeT-Gj_frd0)

Today we talk about requirements and constraints in pip, the differences between the two, and some cases you might use constraints!

## Interactive examples

### Bash

```bash
virtualenv venv
. venv/bin/activate
pip --version

pip install -r requirements.txt
pip uninstall astpretty

pip install -r requirements.txt -c constraints.txt

deactivate
# git clone https://github.com/asottile/re-assert
git clone git@github.com:asottile/re-assert
cd re-assert
nano setup.cfg
tox -e py38

nano tox.ini
grep regex -- setup.cfg
tox -e min
tox -r -e min
```
