# [a virtualenv from nothing! (beginner - intermediate)](https://youtu.be/OXmYKh0eTQ8)

Today I talk about two ways to bootstrap a virtualenv from nothing!

## Interactive examples

### Bash

```bash
python -m venv vvv
ls

python3.9 -m venv venv39
python3.7 -m venv venv37

sudo apt install python3.7-venv
python3.7 -m venv venv37

rm -rf venv37/
python3.7 -m venv venv37
rm -rf venv37/

rm -rf vvv/
time virtualenv vvv

which virtualenv
dpkg -l | grep -- -virtualenv
dpkg -l | grep -- -pip

# curl https://bootstrap.pypa.io/get-pip.py
curl -o virtualenv.pyz https://bootstrap.pypa.io/virtualenv.pyz
python virtualenv.pyz venv

rm -rf venv/
time python virtualenv.pyz venv
```
