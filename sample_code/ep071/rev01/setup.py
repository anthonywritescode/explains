from setuptools import setup
from setuptools import find_packages


setup(
    name='mypkg',
    version='0.0.0',
    packages=find_packages(exclude=('tests*', 'testing*')),
)
