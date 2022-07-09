# [debugging a real issue and googling (beginner - intermediate)](https://youtu.be/IQsat6EA0-M)

Today I walk through the process I'd use when encountering a real problem in python.  I show how I take apart a stacktrace, how I search for the issue, and ultimately find the workaround

## Interactive examples

### Python

```python
from google.cloud import secretmanager
```

### Bash

```bash
uname -a

virtualenv venv -ppython3.10
. venv/bin/activate

pip install google-cloud-secret-manager
python

pip uninstall grpcio
pip install grpcio --no-binary :all:

file venv/lib/python*/site-packages/grpc/_cython/cygrpc.cpython*.so
```
