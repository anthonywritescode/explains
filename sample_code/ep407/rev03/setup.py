from setuptools import setup, find_packages

setup(
    name='example',
    packages=find_packages(),
    py_modules=['b'],
    entry_points={
        'console_scripts': ['a-main=a.main:main'],
    },
)
