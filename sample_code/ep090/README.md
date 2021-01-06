# [making a regex not match itself! (intermediate)](https://youtu.be/4KLLctC0G6U)

Today I show a few situations where you'd want a regex to not match itself as well as a few solutions to make the pattern not match!

## Interactive examples

### Bash

```bash
git init .
nano .pre-commit-config.yaml
git add .pre-commit-config.yaml
git status
git commit -m 'add no DONTSHIP hook'

nano t.py
git add t.py
git status

pre-commit run --all-files

pgrep babi
# pgrep <string>

ps -af | grep babi
# ps -af | grep <string>
ps -af | grep '[b]abi'
```
