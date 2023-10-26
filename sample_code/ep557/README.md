# [don't delete from pypi! (yank instead) (intermediate)](https://youtu.be/lUFA_WklFII)

Today we talk about pypi -- and why you shouldn't delete from it!  yanking is the way and we show how it works and what effects it has on people attempting to install!

## Interactive examples

### Bash

```bash
virtualenv -ppython3.11 venv
. venv/bin/activate

pip install codecov-cli'<0.3.7'
pip install codecov-cli==0.3.6
```
