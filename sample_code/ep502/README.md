# [--extra-index-url is unsafe! (intermediate)](https://youtu.be/fWquXVcTKjU)

Today I go over the `--extra-index-url` parameter, why it is unsafe, some mitigations, and ultimately my recommendation instead.

## Interactive examples

### Bash

Session 1:

```bash
virtualenv venv
. venv/bin/activate

pip install pypiserver

mkdir local
mkdir public

pip download pre-commit --dest public
ls public/

mkdir my-library/
cd !$
nano setup.py
touch my_library.py

python setup.py sdist bdist_wheel
ls dist/

cp dist/my_library-1.0* ../local/

# pip install --index-url https://pypi.org/simple
pip install --index-url http://localhost:9001/simple --extra-index-url http://localhost:9002/simple my-library pre-commit

NO_PWND=1 python setup.py sdist

ls dist/
cp dist/my_library-1000.0.tar.gz ../public/

virtualenv venv2
. venv2/bin/activate
pip install --index-url http://localhost:9001/simple --extra-index-url http://localhost:9002/simple my-library pre-commit
pip install --index-url http://localhost:9002/simple --extra-index-url http://localhost:9001/simple my-library pre-commit
pip install --index-url http://localhost:9002/simple --extra-index-url http://localhost:9001/simple my-library==1 pre-commit
```

Session 2:

```bash
./venv/bin/pypi-server run --port 9001 public/
```

Session 3:

```bash
./venv/bin/pypi-server run --port 9002 local/
```
