# [a python plugin system via entrypoints (intermediate)](https://youtu.be/fY3Y_xPKWNA)

Today I show how to use importlib.metadata + setuptools entrypoints to build a small plugin system!

## Interactive examples

### Notes

`importlib.metadata` was added in python 3.8. If you're using an older version, you'll need to install `importlib_metadata`, a backport of it.

### Python

```python
import importlib.metadata
importlib.metadata.entry_points()
importlib.metadata.entry_points()['hello_world.output']
importlib.metadata.entry_points()['hello_world.output'][0]
importlib.metadata.entry_points()['hello_world.output'][0].load()
```

### Bash

```bash
virtualenv venv
. venv/bin/activate

cd hello-world
pip install -e .
nano venv/bin/hello-world
venv/bin/hello-world

pip install -e .
hello-world
hello-world --outputer wat

pip install -e ../hello-world-json/
hello-world --output json
hello-world --output wat

ls hello_world.egg-info/entry_points.txt
```
