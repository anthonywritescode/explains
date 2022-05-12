from setuptools import setup

setup(
    name='tzname',
    version='1',
    py_modules=['tzname'],
    entry_points={
        'console_scripts': ['tzname=tzname:main'],
    },
)
