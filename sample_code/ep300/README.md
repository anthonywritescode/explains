# [what are python doctests? (beginner - intermediate)](https://youtu.be/37TJeMLyi5I)

Today I talk about python doctests, how you can write and run them (including with pytest!)

## Interactive examples

### Python

```python
square(5)
square(0)
```

### Bash

```bash
virtualenv venv
. venv/bin/activate
pip install pytest

pytest t.py
python -i t.py

python -m doctest -f -v t.py
pytest --doctest-modules t.py
pytest --doctest-modules t.py -v
```
