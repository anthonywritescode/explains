# [can cpython be 76% faster by changing hash()? (no) (intermediate)](https://youtu.be/_8FHjmv8ix0)

Today I analyze / address an impressive claim -- that cpython's hash can be changed and improve performance drastically!

## Interactive examples

### Python

```python
import uuid

foos = [hash(str(uuid.uuid4())) for i in range(100_000)]
foos = [hash(str(uuid.uuid4()) * 1000) for i in range(100_000)]
```

### Bash

Session 1:

```bash
./python ../xxhash-cpython/benchmark.py
```

Session 2:

```bash
git status
git checkout -- benchmark.py
./python benchmark.py
./prefix/bin/pyperf compare_to ../cpython/cp.json xx.json

nano benchmark.py
./python benchmark.py
```
