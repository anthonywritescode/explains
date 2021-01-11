# [testing functools.lru\_cache with pytest! (beginner - intermediate)](https://youtu.be/ujRo8n0LsU4)

Today I talk about how to test a function which is decorated with `lru_cache` with pytest!

## Interactive examples

### Python

```python
import shutil
shutil.which('ruby')
shutil.which('alksdjflkajsdf')
```

### Bash

```bash
virtualenv venv
. venv/bin/activate
pip install pytest

pytest t.py
pytest t.py -v
pytest t2.py -v
```
