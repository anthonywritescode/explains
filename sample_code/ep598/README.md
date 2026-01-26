# [automatic python types!](https://youtu.be/YTDpiP1-PRg)

I wrote a new tool to automatically add python type annotations -- it seems to work pretty well!

## Interactive examples

### Bash

```bash
virtualenv venv
. venv/bin/activate

pip install mypy
dmypy run t.py
dmypy run t.py
dmypy suggest t.f
dmypy suggest t.add

virtualenv venv313 -ppython3.13
./venv313/bin/pip install pyannotate
./venv313/bin/pyannotate --help

dmypy suggest t.add --json
pip install auto-type-annotate

auto-type-annotate t.py
nano t.py

dmypy run
pip install auto-type-annotate
auto-type-annotate --application-directories .:src $(git ls-files -- '*.py' | grep '/issues/')
git diff
```
