# [when should I pin deps: never and always! (intermediate)](https://youtu.be/WSVFw-3ssXM)

Fine I'll make a video about it -- here's my stance on pinning dependencies and why I do what I do in the different scenarios.

## Interactive examples

### Python

```python
import classify_imports

classify_imports.classify_base('cfgv')
classify_imports.classify_base('pre_commit')
classify_imports.classify_base('os')
classify_imports.classify_base('__future__')
```

### Bash

```bash
nano setup.cfg
git grep import

virtualenv venv
. venv/bin/activate
pip install classify-imports

tail -n999 require*.txt
```
