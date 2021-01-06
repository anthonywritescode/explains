# [file modes and chmod (beginner - intermediate)](https://youtu.be/BrBHUosstHg)

Today I talk about the basic modes (read/write/execute) as well as the permission levels (user/group/other) for posix files!

## Interactive examples

### Python

```python
bin(0o750)
```

### Bash

```bash
touch a
mkdir d
ls -al
chmod
umask

chmod 750 a
ls -al
nano a
./a

chmod -x a
./a
ls -al a

groups
sudo chgrp pcrunner a
# sudo chgrp <groupname> <filename>
ls -al a
sudo -u pcrunner cat a
sudo -u nobody cat a

touch d/{1,2,3}
ls d/

ls -al d/
sudo -u nobody ls -al d

chmod o-x d
sudo -u nobody ls -al d

umask 0022
umask

touch x
ls -al x

umask 000
touch x2
ls -al !$

umask 002
touch x3
ls -al !$
```
