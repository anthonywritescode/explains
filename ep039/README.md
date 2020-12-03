# [releasing a python package to pypi (beginner - intermediate)](https://youtu.be/Gre2W5z4iLE)

Just a quick version bump and upload and the steps I take to do that.

## Setup commands

```bash
virtualenv venv

. venv/bin/activate

pip install twine

git clone git@github.com:<your_github_username>/<package_name>
```

## Interactive examples

### Bash

```bash
cd <package_name>
git show v1.4.16

nano setup.cfg
git status
git diff
git add -u
git commit -m 'v1.4.17'
git tag !$
git show

python setup.py sdist bdist_wheel
twine upload -r pypi dist/<package_name>-1.4.17*

git push origin HEAD --tags
```
