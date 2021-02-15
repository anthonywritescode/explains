from setuptools import setup


setup(
    name='uuidcffi',
    version='1',
    py_modules=['uuidcffi'],
    install_requires=['cffi'],
    setup_requires=['cffi'],
    cffi_modules=['build_uuidcffi.py:ffibuilder'],
)
