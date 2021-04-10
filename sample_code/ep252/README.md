# [packaging python typed code (intermediate)](https://youtu.be/n4GJ8rp6DpE)

Today I talk about how to package up typed code -- either inline types or typing stubs and distribute it via pypi!

## Interactive examples

### Bash

```bash
git clone git@github.com:asottile/all-repos
# git clone https://github.com/asottile/all-repos
cd all-repos/

ls
nano all-repos/config.py
nano setup.cfg

ls all_repos/
touch all_repos/py.typed
nano setup.py

virtualenv venv
. venv/bin/activate
pip install setup-py-upgrade

setup-py-upgrade .
git diff

python setup.py sdist bdist_wheel
cd dist/
ls

tar --list -f all_repos-*.tar.gz
tar --list -f all_repos-*.tar.gz | grep 'py\.typed'

unzip -l all_repos-*.whl
unzip -l all_repos-*.whl | grep 'py\.typed'

cd ..

mkdir -p all_repos-stubs/all_repos
cp all-repos/all_repos/util.pyi all_repos-stubs/all_repos
touch all_repos-stubs/__init__.pyi
nano all_repos-stubs/setup.py
```
