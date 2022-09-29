# [avoiding shell injection in github actions (intermediate)](https://youtu.be/7w0Ns8C1shQ)

Today I show a quick little tip to avoid shell injection in github actions pipelines!

## Interactive examples

### Bash

```bash
x='hello " world'
python -c 'import sys; print(sys.argv)' -- "$x"
```
