# [finding regressions with git bisect (intermediate)](https://youtu.be/C2C7FTI8nB4)

Today I explain `git bisect` and how you can use it to find regressions / changes in git repositories automatically!

## Interactive examples

### Python

```python
a()
```

### Bash

```bash
git clone https://github.com/PyCQA/pycodestyle
cd pycodestyle
python -m pycodestyle t.py
python -m pycodestyle t.py --ignore W191
git checkout 2.5.0
python check.py
git checkout master
git checkout -- pycodestyle.py
git status
git bisect
git bisect start
git status
git bisect good 2.5.0
git bisect bad origin/master
git bisect run python check.py
```
