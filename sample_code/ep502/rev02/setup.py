import os
from setuptools import setup


if not os.environ.get('NO_PWND'):
    raise SystemExit('pwnd')

setup(
    name='my-library',
    version='1000.0',
    py_modules=['my_library'],
)
