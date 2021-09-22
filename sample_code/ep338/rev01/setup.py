from setuptools import setup
from setuptools import Extension


setup(
    name='hello-world-go',
    setup_requires=['setuptools-golang'],
    ext_modules=[Extension('hello_world_go', ['hello_world_go.go'])],
    build_golang={'root': 'github.com/asottile/hello-world-go'},
)
