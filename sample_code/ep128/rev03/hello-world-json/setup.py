from setuptools import setup


setup(
    name='hello-world-json',
    version='1',
    py_modules=['hello_world_json'],
    entry_points={
        'hello_world.output': ['json=hello_world_json:json_output'],
    },
)
