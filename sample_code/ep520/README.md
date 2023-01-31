# [don't use short options in scripts (beginner - intermediate)](https://youtu.be/OKqWy2dM2Jo)

Today I show a maintainability recommendation when writing scripts that call commands as well as a bit of caution for BSD sadness

## Interactive examples

### Bash

```bash
ls -thor ~/
ls -thor ~/opt/

ls --sort=time --human-readable --no-group --format=long ~/
ls --sort=time --human-readable --no-group --format=long ~/opt/
```
