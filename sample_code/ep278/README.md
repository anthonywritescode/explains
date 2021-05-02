# [use the clipboard from the terminal (beginner)](https://youtu.be/-ebWr_C29_c)

Today I show two quick and easy commands to utilize the clipboard from the terminal!

## Interactive examples

### Bash

```bash
man xclip
echo hi | xclip -selection c
echo hi
xclip -o -select c

echo hello > f
cat f
xclip -selection c f
echo hello
xclip -o -selectio c > f2

alias pbcopy='xclip -selection -c'
alias pbpaste='xclip -o -selection -c'
echo hi | pbcopy
pbpaste

virtualenv venv
. venv/bin/activate
pip install importtime-waterfall

importtime-waterfall importtime_waterfall
importtime-waterfall --help
importtime-waterfall importtime_waterfall --har
importtime-waterfall importtime_waterfall --har | xclip -selection c
```
