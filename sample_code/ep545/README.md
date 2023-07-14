# [every Dockerfile should have this line! (intermediate)](https://youtu.be/kL0q-7alfQA)

Today we're talking about docker again -- and specifically what you want to do to avoid this common mistake and ensure you're not introducing a western bias in your image!

## Interactive examples

### Python

```python
import locale
locale.getpreferredencoding()

import codecs
codecs.lookup('ANSI_X3.4-1968')

print('\u2603')
```

### Bash

```bash
gcc t.c
./a.out

echo $LANG
LANG= ./a.out

docker run --rm -ti ubuntu:trusty
python3 --version
echo $LANG
python3
exit

docker run -v $PWD/a.out:/mybin:ro --rm -ti ubuntu:jammy
/mybin

export LANG=C.UTF-8
/mybin
exit

docker build -t test .
docker run --rm test bash -c 'echo $LANG'
```
