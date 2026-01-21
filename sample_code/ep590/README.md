# [your tests should have 100% coverage](https://youtu.be/70T6OxKwxm0)

today I make the case for 100% coverage... in tests (and show some interesting cases at work where tests simply weren't running or weren't testing what was expected!)

## Setup commands

```bash
virtualenv venv
. venv/bin/activate
pip install coverage

git clone git@github.com:getsentry/sentry
cd sentry/
```

## Interactive examples

### Bash

```bash
mkdir cov
cd !$

cp <directory>/*.zip .
ls *.zip | cut -d. -f1 | xargs --replace bash -c 'mkdir {} && cd {} && unzip ../{}.zip && mv .coverage ../.coverage.{} && mv .coverage.* ..'

cd ..
git apply
git diff

git fetch origin <commit_hash>
git checkout FETCH_HEAD
git rev-parse HEAD

rm .coverage*; cp cov/.coverage* . && coverage combine
coverage report --include 'tests/**'
coverage report --include 'tests/snuba/sessions/**'
```
