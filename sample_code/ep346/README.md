# [what is umask? (intermediate)](https://youtu.be/ZfDbUxH99n0)

Today I talk about umask and what values make the most sense and why it matters for security!

## Interactive examples

### Bash

```bash
touch foo && mkdir dir
ls -al

umask
umask 0000
umask

rm -r dir foo
touch foo && mkdir dir
ls -al

umask 0002
rm -r dir foo
touch foo && mkdir dir
ls -al

umask 0777
rm -r dir foo
touch foo && mkdir dir
ls -al

nano ~/.bashrc
man umask
```
