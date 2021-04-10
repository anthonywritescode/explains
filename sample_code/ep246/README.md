# [testing output with pytest (beginner - intermediate)](https://youtu.be/dN-pVt7i4Us)

Today I talk about how to test output using pytest -- using the `capsys` and `capfd` fixtures (and why they're different)

## Interactive examples

### Bash

```bash
virtualenv venv
. venv/bin/activate
pip install pytest

python t.py anthony
pytest t_test.py
pytest t_test.py -v
python t.py jeff
```
