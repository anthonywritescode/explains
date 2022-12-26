# [how should I organize my project? (beginner)](https://youtu.be/QGAuwlQ9Gxc)

Today I give my advice for how to organize your project: aka don't worry about it and start hacking!

## Interactive examples

### Bash

```bash
all-repos-find-files --output-paths setup.cfg | xargs grep -l 'py_modules =' | wc -l
all-repos-find-files --output-paths setup.cfg | xargs grep -l 'packages =' | wc -l
```
