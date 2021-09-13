# [what is `source` and why? (beginner - intermediate)](https://youtu.be/YE6ZDpRcdQU)

Today I talk about the `source` command -- why it exists, and why I prefer `.` over `source`!

## Interactive examples

### Bash

Session 1:

```bash
virtualenv venv
nano venv/bin/activate

venv/bin/activate
chmod +x !$
./venv/bin/activate
chmod -x venv/bin/activate

. venv/bin/activate
echo $PATH

type deactivate
deactivate
```

Session 2:

```bash
chmod +x .env
ls -al
./.env

cat !$
echo "$FOO"

chmod -x .env

source .env
echo $FOO
echo $SECRET
```
