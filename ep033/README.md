# [what is a shebang (#!)? (beginner - intermediate)](https://youtu.be/g3VxRdtlMoE)

Today I explain what a shebang is on posixlike platforms and how the OS decides what is executable.  I also show a bit how windows doesn't support this and how it decides what is executable.

## Interactive examples

### Bash

```bash
ls /usr/bin
ls -al /usr/bin/zip
ls -al /usr/bin/ls

./t.sh
ls -al t.sh
chmod +x t.sh
./t.sh
mv t.sh t.py
./t.py

env
env X=1 bash -c 'echo $X'
env X=124 bash -c 'echo $X'
env bash
exit
```

### Windows CMD

```batch
echo %PATH%
echo %PATHEXT%
cat t.py
t.py
```
