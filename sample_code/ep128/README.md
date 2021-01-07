# [a python plugin system via entrypoints (intermediate)](https://www.youtube.com/watch?v=fY3Y_xPKWNA)

Today I show how to use importlib.metadata + setuptools entrypoints to build a small plugin system!

## Note

`importlib.metadata` was added in python 3.8. If you're using an older version, you'll need to install `importlib_metadata`, a backport of it.

[Here's an example](https://github.com/pre-commit/pre-commit/blob/7432acc2157c995b88d70d1cd0b3609c32364eed/pre_commit/constants.py#L3-L6) of how to handle imports if you need to support both, and [here's an example](https://github.com/pre-commit/pre-commit/blob/7432acc2157c995b88d70d1cd0b3609c32364eed/setup.cfg#L32) of how to add it as a dependency.
