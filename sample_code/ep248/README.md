# [one-off 3rd party mypy types (intermediate)](https://youtu.be/mKmmZHMwXAY)

Today I show how to fix "Cannot find implementation or library stub for module named ..." errors in mypy by writing our own custom .pyi stubs!

## Interactive examples

### Bash

Session 1:

```bash
git clone git@github.com:asottile/markdown-code-blocks
# git clone https://github.com/asottile/markdown-code-blocks

cd markdown-code-blocks
virtualenv venv
. venv/bin/activate
pip install mypy

mypy markdown_code_blocks.py

mkdir stubs

cat << EOF
# Include this configuration to setup.cfg:

[mypy]
mypy_path = stubs
EOF

pip install mistune
pip uninstall mistune

mkdir stubs/mistune
touch !$/__init__.pyi

babi stubs/mistune/renderers.pyi
babi stubs/mistune/markdown.pyi

mypy markdown_code_blocks.py --ignore-missing-imports

tree stubs/
```

Session 2:

```bash
virtualenv venv2
. venv2/bin/activate
pip install 'mistune>=2.0.0a5'

ls venv2/lib/python*/site-packages
```
