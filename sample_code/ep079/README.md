# [why not global pip / virtualenv? (intermediate)](https://youtu.be/O390_abzo08)

Today I talk about three reasons why I don't install pip or virtualenv globally on my linux systems!  I also show how I set up my machine to avoid both of those.

## Interactive examples

### Bash

Session 1:

```bash
docker run --rm -ti ubuntu:focal bash
apt update && apt install virtualenv

virtualenv venv
rm -rf venv/

virtualenv venv
venv/bin/pip freeze
venv/bin/pip uninstall distlib
venv/bin/pip freeze
exit

dpkg -l | grep python3-
aptitude why python3-urllib3
```

Session 2:

```bash
virtualenv --version
virtualenv venv
./venv/bin/pip freeze

rm -rf ~/opt/venv/
hash -r
which virtualenv
virtuaelnv venv

curl --location --output virtualenv.pyz https://bootstrap.pypa.io/virtualenv.pyz
python virtualenv.pyz ~/opt/venv
~/opt/venv/pip install virtualenv
ls -al ~/bin/virtualenv
which virtualenv
```
