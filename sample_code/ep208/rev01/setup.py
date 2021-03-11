from setuptools import Extension
from setuptools import setup


setup(
    name='simple-c-extension',
    version='1',
    ext_modules=[Extension('sample_c_extension', ['sample_c_extension.c'])],
)
