# [python executable zipapps (intermediate)](https://youtu.be/HfL2s2JySos)

Today I explain jar-like zipapps -- a convenient way to distribute a python application in a single file!

## Interactive examples

### Python

```python
import astpretty
import ast
astpretty.pprint(ast.parse("print('hello')"))
```

### Bash

```bash
zip out.zip __main__.py
python out.zip
python virtualenv.pyz venv
chmod +x out.zip
echo '#!/usr/bin/env python' >> out2.zip
cat out.zip >> out2.zip
chmod +x out2.zip
file out2.zip
head -1 out2.zip
./out2.zip

. venv/bin/activate
pip download astpretty
mkdir x
cd !$
unzip ../*.whl
cd ..
rm -rf x/
PYTHONPATH=<astpretty_wheel_filename_here>.whl python
PYTHONPATH=<astpretty_wheel_filename_here>.whl python -m astpretty __main__.py
```
