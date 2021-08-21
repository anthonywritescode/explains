# [smaller / faster builds with dockerignore (beginner - intermediate)](https://youtu.be/dEZ5WVWLris)

Today I show a quick easy best practice when working with docker: setting up a `.dockerignore`!

## Interactive examples

### Bash

```bash
virtualenv venv
. venv/bin/activate

pip install pytest coverage flake8 pre-commit

git init .
git commit --allow-empty -m "empty commit"

python -m app
docker build -t app .

ls
ls -al .git

docker run --rm -ti app bash
ls -al
exit

mv .dockerignore ..
time docker build -t app .

mv ../.dockerignore .
time docker build -t app .

docker run --rm -ti app bash
ls -al
exit
```
