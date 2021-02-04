from setuptools import setup
from setuptools import Extension


setup(
    name='hello-world',
    version='1',
    ext_modules=[
        Extension(
            '_hello_world',
            ['_hello_world.c'],
            py_limited_api=True,
            define_macros=[('Py_LIMITED_API', None)],
        ),
    ],
)
