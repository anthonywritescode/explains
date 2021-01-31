from setuptools import setup


setup(
    name='hello-world',
    version='1',
    entry_points={
        'console_scripts': ['hello-world=hello_world:main'],
    }
)
