# [how to get pip for deadsnakes / docker pythons (intermediate)](https://youtu.be/2Hg5-Hrsa6w)

Today I talk about the various ways to acquire pip for pythons -- specifically in docker for deadsnakes (though these approaches should also work for normal system pythons)

## Interactive examples

### Bash

```bash
ls -al $(which docker)
docker build -t base .
docker run --rm -ti base bash

python3.10
pip
pip3
pip3.10
python3.10 -m pip

docker build -f Dockerfile.venv -t base-venv .
docker run --rm -ti base-venv bash

which pip
pip install pre-commit

/usr/bin/python3.10 -m ensurepip
which pip3.10
rm -rf /venv/
which pip3.10
ls /usr/local/bin/
exit

docker build -f Dockerfile.ensurepip -t base-ensurepip .
# docker run --rm -ti base-ensurepip bash

docker build -f Dockerfile.debian -t base-debian .
docker run --rm -ti base-debian bash

python3.10 -m pip install astpretty
apt update && apt install python3.10-distutils
python3 -m pip install html5lib
exit

docker build -f Dockerfile.get-pip -t base-get-pip .
docker run --rm -ti base-get-pip bash

pip3.10 install astpretty
```
