# [are your python tests even running? (intermediate)](https://youtu.be/0nPS_vVmhp0)

Today I go over an extremely common pitfall with pytest and a helpful fix to prevent this from happening to you!

## Interactive examples

### Bash

```bash
virtualenv venv
. venv/bin/activate
mkdir tests

nano tests/whatever_module_test.py

pip install pytest
pytest tests
pytest tests -v

cp tests/whatever_module_test.py tests/tests.py
pytest tests
pytest tests/tests.py

pytest --help | less
git init .
pre-commit sample-config > .pre-commit-config.yaml
pre-commit autoupgrade

git status
git add tests .pre-commit-config.yaml
git rm -r tests/__pycache__/
git rm -rf tests/__pycache__/
git status

git commit -m 'add tests'
pre-commit run --all-files

nano pytest.ini
pytest tests

rm pytest.ini
git mv tests/tests.py tests/whatever_test.py
pytest tests

nano .pre-commit-config.yaml
pre-commit run --all-files
```
