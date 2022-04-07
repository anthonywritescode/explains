# [3 ways to clear / fix the terminal (beginner)](https://youtu.be/LSEnVCBnKN4)

Today I show three ways to fix / clear the terminal (also featuring a bug in poetry!)

## Interactive examples

### Bash

```bash
echo
echo hi
echo hello hello

clear
clear | hd -c
echo -e '\033[H\033[2J\033[3J'
echo -n -e '\033[H\033[2J\033[3J'

# Ctrl-l

virtualenv venv
. venv/bin/activate
pip install poetry

poetry init
echo hi
clear

reset
```
