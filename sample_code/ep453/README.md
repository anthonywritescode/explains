# [bash strict mode gotcha (intermediate)](https://youtu.be/oqq5k8XsrSs)

I ran into a surprising case at work where bash strict mode didn't catch a script failure!  I show the class of error and how you can detect it with linters

## Interactive examples

### Bash

```bash
bash t.sh
echo $?

virtualenv venv
. venv/bin/activate
pip install shellcheck-py

shellcheck t.sh
shellcheck t.sh --enable=all
```
