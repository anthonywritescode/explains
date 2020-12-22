# [python packaging: data files (intermediate)](https://youtu.be/bfyIrX4_yL8)

Today I talk about packaging data / build files for python packages!  This covers MANIFEST.in, include_package_data, package_data, source distributions and wheels!

## Interactive examples

### Bash

```bash
mkdir mypkg
touch !$/__init__.py
touch mypkg/main.py

virtualenv venv
. venv/bin/activate

python setup.py sdist bdist_wheel
ls dist/
cd dist/
unzip -l *.whl
tar --list -f *.tar.gz

cd ..
rm -rf dist/

rm -rf build/ dist/ *.egg-info mypkg/foo.py && python setup.py sdist bdist_wheel && unzip -l dist/*.whl && tar --list -f dist/*.tar.gz

cd dist/
pip wheel *0.0.0.tar.gz
cd ..

touch LICENSE
mkdir mypkg/pkg1
touch !$/__init__.py
nano mypkg/pkg1/t.json
```
