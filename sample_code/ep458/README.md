# [what release was this fixed? (workflow) (intermediate)](https://youtu.be/7f3UdjuQYtw)

Today I walk through a workflow I use pretty often to find "when did this change?" and "when was this released?"

## Interactive examples

### Bash

Session 1:

```bash
virtualenv venv37 -ppython3.7
. venv/bin/activate
pip install zope.interface==4.6.0

virtualenv venv -ppython3.9
. venv/bin/activate
pip install zope.interface==4.6.0
pip install zope.interface
pip install zope.interface=4.7.2
```

Session 2:

```bash
git clone https://github.com/zopefoundation/zope.interface
cd zope.interface/
nano setup.py

git log -G Feature -- setup.py
git log -p -G Feature -- setup.py
git describe --contains <commit_hash>
```
