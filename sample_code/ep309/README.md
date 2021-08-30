# [importing non-module python files (intermediate)](https://youtu.be/B5bToFdBxdw)

Today I show how to import non-modules in python -- either with invalid module names or files which aren't .py at all!

## Interactive examples

### Python

```python
import foo-bar
import foo_bar

__import__('foo-bar')

import entry
__import__('entry')

import importlib.machinery
import importlib.util

# loader = importlib.machinery.SourceFileLoader('entry', './entry')
loader = importlib.machinery.SourceFileLoader('entry', 'entry')
spec = importlib.util.spec_from_loader(loader.name, loader)

loader
spec

mod = importlib.util.module_from_spec(spec)
mod
mod.main

loader.exec_module(mod)
mod.main()

loader = importlib.machinery.SourceFileLoader('entry', 'entry')
spec = importlib.util.spec_from_loader(loader.name, loader)
mod = importlib.util.module_from_spec(spec)
loader.exec_module(mod)
```

### Bash

```bash
python foo-bar.py
chmod +x entry
./entry
```
