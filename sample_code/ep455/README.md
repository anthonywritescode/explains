# [pip freezing (==) isn't safe (intermediate)](https://youtu.be/oGpyupM52IQ)

Today I walk through why == pinning isn't enough to ensure repeatability through an *intentional* feature.  personally, I hope this "feature" gets removed

## Interactive examples

### Bash

Session 1:

```bash
virtualenv venv
. venv/bin/activate

pip install pypiserver
pip download pre-commit --dest wheels
pypi-server run ./wheels
```

Session 2:

```bash
curl -v http://localhost:8080/simple
curl http://localhost:8080/simple/

mkdir src
cd !$

virtualenv venv
. venv/bin/activate

pip install pre-commit --index-url http://localhost:8080/simple
pip freeze > requirements.txt
pip freeze --all > requirements.txt

deactivate
rm -rf venv/
nano requirements.txt

# Session 3 steps

virtualenv venv/
. venv/bin/activate

pip install -r requirements.txt --index-url http://localhost:8080/simple
pre-commit --version
```

Session 3:

```bash
git clone git@github.com:pre-commit/pre-commit
cd pre-commit/

echo "print('pwnd')" > pre_commit/__init__.py
pip wheel . --no-deps --build-opt=--build-number=1

ls pre_commit*.whl
cp pre_commit*.whl ../wheels/

curl http://localhost:8080/simple/pre-commit/
```
