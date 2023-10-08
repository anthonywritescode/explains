# [stopping xargs early (intermediate)](https://youtu.be/-J36ki4rU_Q)

Today we talk about a debugging technique using xargs -- and making it stop on the first failure

## Interactive examples

### Bash

```bash
pytest --collect-only -q tests/sentry/integrations/slack/test_tasks.py > testlist

xargs -a testlist -d'\n' -n1 echo
xargs -a testlist -d'\n' -n1 echo pytest -qq
xargs -a testlist -d'\n' --replace bash -xc 'pytest -qq {} || exit 255'
```
