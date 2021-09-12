# [making an omni-executable (intermediate)](https://youtu.be/r41t-t27V9c)

Today we talk about what an omni-executable is, show a popular example (busybox) and then write one ourselves!

## Interactive examples

### Python

```python
import os
os.readlink('uniq2')
os.readlink('/tmp/explains/uniq2')
```

### Bash

```bash
docker run --rm -ti busybox sh
ls /bin
ls -al /bin
sha256sum /bin/*

echo $'foo\nbar' | uniq
echo $'foo\nfoo\nbar' | uniq
echo $'foo\nfoo\nbar' | unix2dos

ln -s /bin/vi uniq
echo $'foo\nfoo\nbar' | ./uniq
exit

chmod +x t.py
./t.py

ln -s t.py uniq
./uniq

echo $'foo\nfoo\nbar' | ./uniq
echo $'foo\nfoo\nbar' | ./t.py

ln -s uniq uniq2
ls -al

echo $'foo\nfoo\nbar' | ./uniq
echo $'foo\nfoo\nbar' | ./uniq2
```
