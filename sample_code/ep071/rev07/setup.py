import json

from setuptools import setup
from setuptools import find_packages
from setuptools.command.build_py import build_py


class my_build_py(build_py):
    def run(self) -> None:
        with open('mypkg/foo.json') as f:
            contents = json.load(f)
        with open('mypkg/foo.py', 'w') as f:
            f.write(f'JSON = {contents!r}\n')
        super().run()


setup(
    name='mypkg',
    version='0.0.0',
    packages=find_packages(exclude=('tests*', 'testing*')),
    cmdclass={'build_py': my_build_py},
    package_data={
        'mypkg': ['*.json', 'pkg1/*.json'],
        # 'mypkg.pkg1': ['*.json'],
    }
)
