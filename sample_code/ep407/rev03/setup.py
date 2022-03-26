from setuptools import setup, find_packages

setup(
    name='example',
    packages=find_packages(),
    py_module=['b'],
    entry_points={
        'console_scripts': ['a-main=a.main:main'],
    },
)
