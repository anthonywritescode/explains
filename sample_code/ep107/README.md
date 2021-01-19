# [pure python windows .exe (no compiler!) (intermediate)](https://youtu.be/nzaH5n-Xk64)

I've found a really cool way to make pure python executables (.exe) for windows!

## Interactive examples

### Bash

```bash
zip out.pyz __main__.py
python out.pyz

virtualenv venv
. venv/bin/activate
pip install distlib

touch out.exe
file !$
cat venv/lib/python3.8/site-packages/distlib/t32.exe >> out.exe
# cat venv/Lib/site-packages/distlib/t32.exe >> out.exe

echo '#!python.exe' >> out.exe
cat out.pyz >> out.exe
file out.exe
```
