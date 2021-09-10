# [pip install from git (beginner - intermediate)](https://youtu.be/AQrskWh-F5E)

Today I show how to install python packages from git using pip -- I also show the tricky syntax needed to install from git over ssh (such as for private repositories)

## Interactive examples

### Bash

```bash
virtualenv venv
. venv/bin/activate

pip install astpretty
pip uninstall astpretty

pip install git+https://github.com/asottile/astpretty
pip uninstall astpretty

pip install git+https://github.com/asottile/astpretty@3e43d8e126a9f2bbf5f28c674b4478731e6d54b1
pip uninstall astpretty

git clone git@github.com:asottile/astpretty
pip install git+ssh://git@github.com/asottile/astpretty
```
