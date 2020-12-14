from setuptools import find_packages
from setuptools import setup


setup(
    name='hello-world',
    version='1.0.0',
    description='this package contains some sample hello world code',
    author='Anthony Sottile',
    author_email='email@example.com',
    url='https://github.com/asottile/hello-world',
    # install_requires=[],
    # packages=['hello_world'],
    packages=find_packages(exclude=('tests*', 'testing*')),
    entry_points={
        'console_scripts': [
            'hello-world-cli = hello_world.main:main',
        ],
    },
)
