# [testing optional python dependencies (intermediate)](https://youtu.be/PXu3KCMT3l4)

Today I talk about how to test optional dependencies!  In this example I go over how to add an optional configuration loader and then test the various scenarios with pytest!

## Interactive examples

### Python

```python
import sys
sys.modules['toml'] = None
import toml
```

### Bash

```bash
python main.py
touch config.json
nano config.json

mv {,not}config.json
python main.py

mv {not,}config.json
python main.py

mv {,not}config.json
nano config.toml
python main.py

virtualenv venv
. venv/bin/activate
pip install toml
python main.py

pip install pytest
pytest inline_test.py
pytest module_scoped_test.py
```
