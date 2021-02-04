from setuptools import setup
from setuptools import Extension


setup(
    name='hello-world',
    version='1',
    ext_modules=[Extension('_hello_world', ['_hello_world.c'])],
)
