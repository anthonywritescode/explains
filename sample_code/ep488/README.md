# [python os / platform-specific deps (PEP 508) (intermediate)](https://youtu.be/cNQhpprVyn0)

Today I talk about conditional dependencies for platform-specific deps using environment markers!

## Interactive examples

### Bash

```bash
virtualenv venv
. venv/bin/activate

pip install -r requirements.txt
```

### Windows CMD

```batch
rm -rf venv
python -m venv venv
venv\Scripts\activate

pip install -r requirements.txt
```
