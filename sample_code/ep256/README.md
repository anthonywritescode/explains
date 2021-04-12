# [correct `apt-get` for ubuntu / debian in docker (intermediate)](https://youtu.be/ZAoK8O9oBGo)

Today I show the correct way to use `apt-get` in docker when working with debian-based systems (as well as a common incorrect way)

## Interactive examples

### Bash

Session 1:

```bash
podman images
docker build -t explains-apt-example .
docker run --rm -ti explains-apt-example bash

docker build -t explains-apt-example .
docker images -a
```

Session 2:

```bash
echo hi
python3 --version
exit
```
