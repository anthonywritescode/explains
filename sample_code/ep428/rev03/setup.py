from setuptools import setup

setup(
    name='tzname',
    version='1',
    py_modules=['tzname'],
    install_requires=[
        'backports.zoneinfo;python_version<"3.9"',
    ],
    entry_points={
        'console_scripts': ['tzname=tzname:main'],
    },
)
