# [useful commands: `pstree` (beginner - intermediate)](https://youtu.be/Omu4tXtlULU)

Today I talk about one of the more useful debugging commands `pstree` and a few usecases / demos of it!

## Interactive examples

### Bash

```bash
virtualenv venv
. venv/bin/activate
pip install git-code-debt

git-code-debt-generate
ps -ef | grep git-code-debt
pstree -halp <process_id>
pstree -shlap <process_id>
watch pstree -shlap <process_id>
watch -n.3 pstree -shlap <process_id>
```
