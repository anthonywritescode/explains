# [unconventional uses of dumb-init](https://youtu.be/thqnRzzXZvQ)

dumb-init is a minimal init system for docker containers -- but sometimes it can be really useful outside of them!

## Setup commands

```bash
git clone git@github.com:asottile/pyupgrade
```

## Interactive examples

### Bash

```bash
tmux

virtualenv venv
. venv/bin/activate
pip install dumb-init

dumb-init --help
kill -l

dumb-init --rewrite 28:0 ./bin/run-apache2
dumb-init -v --rewrite 28:0 ./bin/run-apache2

cd pyupgrade/
virtualenv venv
. venv/bin/activate

nano testlists
xargs -d '\n' pytest < testlists

nano tests/main_test.py
dumb-init xargs -d '\n' pytest < testlists

ps -ef | grep pytest
dumb-init -v xargs -d '\n' pytest < testlists
```
