# [python int DoS vulnerability (CVE 2020-10735) (beginner - intermediate)](https://www.youtube.com/watch?v=lIniq12cMK0)

Today we talk about the int conversion denial-of-service vulnerability disclosed by cpython recently as well as the changes to python to mitigate this.

## Interactive examples

### Bash

```bash
time python3 -c 'int("2" + "0" * 10000)'
time python3 -c 'int("2" + "0" * 100000)'
time python3 -c 'int("2" + "0" * 1000000)'
time python3 -c 'int("2" + "0" * 10000000)'
^C^C^C^\

time python3 -c '"2" + "0" * 1000000'
time python3 -c 'str(2 << 10000)'
time python3 -c 'str(2 << 100000)'
time python3 -c 'str(2 << 1000000)'
time python3 -c 'str(2 << 10000000)'
^C

time ./python -c 'int("2" + "0" * 1000000)'
time ./python -c 'int("2" + "0" * 10000000)'
time ./python -c 'int("2" + "0" * 1000000)'
time ./python -c 'int("2" + "0" * 100000)'

time PYTHONINTMAXSTRDIGITS=1000000 ./python -c 'int("2" + "0" * 100000)'
time PYTHONINTMAXSTRDIGITS=10000 ./python -c 'int("2" + "0" * 100000)'
time PYTHONINTMAXSTRDIGITS=0 ./python -c 'int("2" + "0" * 100000)'

./python
```

### Python

```python
import sys
sys.get_int_max_str_digits()
sys.set_int_max_str_digits(123123)
sys.get_int_max_str_digits()
```
