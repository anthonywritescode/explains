# [virtualenv isn't reproducible! (by default) (intermediate)](https://youtu.be/mgJiCnqzYlI)

Today I go over a little wart with virtualenv and how it doesn't always give you the same starting state based on a mysterious background uploader

## Interactive examples

### Bash

```bash
virtualenv venv
virtualenv venv2 --pip=embed --setuptools=embed --wheel=embed --no-periodic-update
# VIRTUALENV_PIP=embed ...
```
