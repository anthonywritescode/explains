# [how I fixed a 9GB memory leak in cargo (rust) (intermediate)](https://youtu.be/uxJhAXdBlbc)

Today I show off a cool bit of debugging and fixing I did at sentry to save a memory leak in cargo!

## Interactive examples

### Bash

Session 1:

```bash
git clone git@github.com:getsentry/symbolic
cd symbolic/

sudo docker run --privileged --rm tonistiigi/binfmt --install arm64

make wheel-manylinux IMAGE=manylinux2014_aarch64

nano py/manylinux.sh

make wheel-manylinux IMAGE=manylinux2014_aarch64
```

Session 2:

```bash
top
# htop

sudo docker ps
sudo docker kill <container_id>
```
