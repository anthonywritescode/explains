# [python cli tested with pytest - (beginner to intermediate)](https://youtu.be/qvkppppy9K8)

I build out a simple skeleton for a command line interface in python and show how to test it with pytest!

thanks to PanosTrak for the question!

## Setup commands

```bash
virtualenv venv

. venv/bin/activate

pip install pytest

# if you want to try babi
pip install babi
```

## Interactive examples

### Python

```python
import hello

dir(hello)
hello.main()

hello.__name__
__name__
```

### Bash

```bash
python -S <<< 'exit'

python -S <<< 'import pytest'

echo $?

bash -c 'exit 2'; echo $?

bash -c 'exit 42'

prev_exit_code=$?

echo "$prev_exit_code"
```
