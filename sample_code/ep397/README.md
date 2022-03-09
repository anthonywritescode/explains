# [python can import from zips! (intermediate)](https://youtu.be/XCMOeFN6zX4)

Today I show a useful technique for zipped code in python and how you can use this to run wheels and more!

## Interactive examples

### Bash

```bash
curl -o virtualenv.pyz https://bootstrap.pypa.io/virtualenv.pyz
file virtualenv.pyz
python virtualenv.pyz --help

ls
rm virtualenv.pyz

mkdir y
babi y/t.py

cd y/
zip ../t.zip *

cd ..
unzip -l t.zip

python  -c 'import t'
PYTHONPATH=t.zip python -c 'import t'
PYTHONPATH=t.zip python -c 'import t; t.f()'

pip download astpretty pip
file astpretty*.whl
PYTHONPATH=astpretty*.whl python -m astpretty --help

pip downlaod pyupgrade
PYTHONPATH=pyupgrade*.whl:tokenize_rt*.whl python -m pypgrade --help

PYTHONPATH=pip*.whl python -m pip install pre-commit --target t
python -m pip --help
```
