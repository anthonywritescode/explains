# [what are python wheels? (intermediate - advanced)](https://youtu.be/4L0Jb3Ku81s)

Today I talk about wheels, what the filename means, how they're built, what the format looks like, and how to install them!

## Interactive examples

### Bash

```bash
ls | xargs --replace echo - {}

virtualenv venv
. venv/bin/activate

pip download astpretty==1.7.0
unzip -l astpretty-1.7.0-py2.py3-none-any.whl

mkdir y
cd !$
unzip ../astpretty-1.7.0-py2.py3-none-any.whl
babi astpretty-1.7.0.dist-info/*

pip download ukkonen==1.0.1 --no-deps
unzip -o ukkonen-1.0.1-cp36-abi3-manylinux_2_5_x86_64.manylinux1_x86_64.manylinux_2_17_x86_64.manylinux2014_x86_64.whl '*/WHEEL'
unzip -p ukkonen-1.0.1-cp36-abi3-manylinux_2_5_x86_64.manylinux1_x86_64.manylinux_2_17_x86_64.manylinux2014_x86_64.whl '*/WHEEL'

pip download babi-grammars==0.0.31
unzip -l babi_grammars-0.0.31-py2.py3-none-any.whl | less

pip install babi_grammars-0.0.31-py2.py3-none-any.whl
ls venv/share/babi/grammar_v1/
ls venv/lib/python3*/site-packages/

pip download greenlet==1.1.2 --python-version=3.8 --platform=manylinux2010_x86_64 --only-binary=:all:
unzip -l greenlet-1.1.2-cp38-cp38-manylinux2010_x86_64.whl | less

pip install greenlet-1.1.2-cp38-cp38-manylinux2010_x86_64.whl
ls venv/include/site/python3*/greenlet/greenlet.h
ls venv/lib/python3*/site-packages/

pip download awscli==1.22.14 --no-deps
unzip -l awscli-1.22.14-py3-none-any.whl | less

unzip -p -l astpretty-1.7.0-py2.py3-none-any.whl */entry_points.txt
pip install astpretty-1.7.0-py2.py3-none-any.whl
nano venv/bin/astpretty

./venv/bin/pip download dumb-init
ls
```
