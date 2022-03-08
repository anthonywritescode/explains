# [my python project setup (+ all tools) (intermediate)](https://youtu.be/q8DkatMZvUs)

Today I go over all the tools I use to set up my projects, as well as the differences between 1-file libraries, multi-file libraries, and applications!

## Interactive examples

### Notes

#### multi-file library

- pre-commmit: manages linters / code formatters
    - .pre-commit-config.yaml
- pre-commit-hooks: out-of-the-box language-agnostic tools
- flake8: python linter framework
- autopep8: code formatter
- reorder-python-imports: import sorter
- pyupgrade: code formatter
- add-trailing-comma: code formatter
- setup-cfg-fmt: code formatter
    - setup.cfg declarative metadata
- mypy: type checker
- `.gitignore`: prevent untracked garbage
- `.azure-pipelines.yml`: continuous integration
- `CHANGELOG.md`: change history
- `LICENSE`: MIT license, initial year for copyright
- `README.md`: talks about the project
- `requirements-dev.txt`: testing dependencies
    - `covdefaults`: coverage plugin
    - `coverage`: code coverage tool
    - `pytest`: testing tool
- `setup.py`: very minimal
    - sometimes more things for non-metadata uses
- `setup.cfg`: declarative metadata
    - `packages: find`: discover the top level packages
    - I personally don't use a `src/` layout
- `tox.ini`: "fancy" make for python
- `{project_name}/`
    - top level of the distributed code
    - `__init__.py`: I don't write any code here
- `tests/`
    - where my tests go
    - I name them `*_test.py` for tab completion
- `testing/`
    - code that's helpful for tests (but not tests)

#### single file library

- `setup.cfg`:
    - `py_modules`: instead of `packages = find:`

#### applications

- `aactivator`: auto virtualenv activator
    - `.activate.sh` `.deactivate.sh`
- no `setup.py`
- `setup.cfg`: does not contain metadata
- `requirements-tools`:
    - similar to `pip-tools`, `pipenv`, `poetry`, etc.
    - `requirements-minimal.txt` `requirements-dev-minimal.txt`: input
       requirements
    - `requirements.txt` `requirements-dev.txt`: pinned versions

### Bash

```bash
# git clone https://github.com/asottile/astpretty
git clone git@github.com:asottile/astpretty

# git clone https://github.com/pre-commit/pre-commit-hooks
git clone git@github.com:pre-commit/pre-commit-hooks

ls

cd pre-commit-hooks
git clean -fxfd
ls -al

cd ../astpretty/

cd ..
cd -

check-requirements
check-requirements -v
upgrade-requirements

git checkout -- .
tree .github/
```
