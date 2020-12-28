from setuptools import setup


setup(
    name='foo',
    version='0.0.0',
    install_requires=['cfgv'],
    extras_require={
        'flask': ['flask', 'flask-wtf'],
        'testing': ['pytest'],
    },
)
