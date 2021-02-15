# [python cffi tutorial (intermediate - advanced)](https://youtu.be/X5irxO5VCHw)

Today I build a sample cffi library, wrapping the `uuid` system module!  cffi is a performant alternative to writing error-prone C extensions and performs well with pypy!

## Interactive examples

### Python

```python
import uuid
uuid.UUID(bytes=b'x' * 16)

import uuidcffi
uuidcffi.generate_uuid()
```

### Bash

```bash
virtualenv venv
. venv/bin/activate

locate uuid.h
dpkg -L uuid-dev
pip install .
```
