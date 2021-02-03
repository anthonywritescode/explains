# [a "hello world" python C extension (intermediate - advanced)](https://youtu.be/HrEzCI3jIHw)

Today I create a sample hello world python C extension and walk through a bit of api and reference counting.

## Interactive examples

### Python

```python
import _hello
_hello.hello_world()

def hello(name, /):
    s = 'hello %s' % name.upper()
    return s

hello('anthony')


import _hello
_hello.hello("foo")
_hello.hello(1)


import _hello
_hello.hello("world")


import _hello
_hello.hello('anthony')

import sys
sys.getrefcount('ANTHONY')


import _hello
_hello.hello("anthony")
```

### Bash

```bash
virtualenv venv
. venv/bin/activate
pip install .
```
