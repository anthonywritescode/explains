# [recursively import python modules (intermediate)](https://youtu.be/t43zBsVcva0)

Today I show how to recursively import all modules in a directory and also show a few use cases I have for this!

## Interactive examples

### Python

```python
import pkg.foo.bar
```

### Bash

```bash
mkdir pkg
touch pkg/{__init__.py,a.py,b.py}

mkdir pkg/d
touch pkg/d/{__init__.py,f.py}

tree pkg

python t.py

mkdir pkg/foo
touch pkg/foo/bar.py
python t.py
```
