# [a python extension in go (advanced)](https://youtu.be/kCRU_ZTcxac)

Today I show how to write a python "C" extension in go!

## Interactive examples

### Python

```python
import hello_world_go

hello_world_go.sum(1000, 337)
hello_world_go.hello('asottile')
```

### Bash

```bash
go mod init github.com/asottile/hello-world-go

virtualenv venv
. venv/bin/activate

python setup.py sdist
tar --list -f dist/hello-world-go-*.tar.gz

pip install dist/hello-world-go-*.tar.gz
rm -rf dist/

pip install .
rm -rf dist/

python setup.py bdist_wheel
ls dist/
unzip -l dist/hello_world_go-*.whl
```
