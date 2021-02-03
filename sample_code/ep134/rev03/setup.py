from setuptools import setup
from setuptools import Extension


setup(
    name='hello-lib',
    version='1',
    ext_modules=[Extension('_hello', ['_hello.c'])],
)
