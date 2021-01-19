# [python dist-packages vs. site-packages (intermediate)](https://youtu.be/aEB_EcgTiQo)

Today I talk about dist-packages / site-packages and the reasons debian has for separating the two.

## Interactive examples

### Bash

Session 1:

```bash
ls /usr/lib/python3/dist-packages
```

Session 2:

```bash
virtualenv venv
ls venv/
ls venv/lib/python3.8/site-packages
# ls venv/Lib/site-packages
```
