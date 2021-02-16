# [customizing "command not found" (intermediate)](https://youtu.be/p4cpVggLuJk)

Today I talk about customizing the "command not found" handler in bash, as well as a productivity hack I (ab)use this for!

## Interactive examples

### Bash

```bash
sdfgsdfgsdfg
unset command_not_found_handle
sdfgsdfgsdfg

command_not_found_handle() { echo "you done goofed: $@"; }
unknown command here
nano ~/.bashrc

command_not_found_handle() {
    if [ -x "venv/bin/$1" ]; then
        echo 'you forgot to activate ./venv -- I gotchu' 1>&2
        exe="venv/bin/$1"
        shift
        "$exe" "$@"
        return $?
    else
        echo "$0: $1: command not found" 1>&2
        return 127
    fi
}

virtualenv venv
. venv/bin/activate
pip install mypy
cat t.py
deactivate
which mypy

. venv/bin/activate
which mypy
deactivate

mypy t.py
wat
```
