# [why pytest.mark.usefixtures? (intermediate)](https://youtu.be/BE2v1VCmGwg)

Today I talk about why I used @pytest.mark.usefixtures instead of normal pytest fixture arguments

## Interactive examples

### Bash

```bash
virtualenv venv
. venv/bin/activate

pip install pytest
pytest t.py

pip install dead
dead

pip install pylint
pylint t.py
```
