# [simple python dockerfile w/ flask (intermediate)](https://youtu.be/8V4UowjLIMc)

Today I make a relatively simple python dockerfile using flask!

## Interactive examples

### Bash

```bash
virtualenv venv
. venv/bin/activate
pip install flask

flask run
pip freeze > requirements.txt

rm -rf venv/ __pycache__/
ls

docker build -t test .
docker run --rm -ti test bash

flask --help
exit

docker build -t test .
docker run --rm test flask run
docker run -p 5000:5000 --rm test flask run --host=0.0.0.0
curl http://127.0.0.1:5000 && echo
```
