# [how can an identical docker image produce different results?](https://youtu.be/CBbgmRAg0VM)

isn't that the whole point of docker?  build once run anywhere?

## Interactive examples

### Bash

Session 1:

```bash
mkdir y
touch y/a
ln -s y/a y/b
tree y

ln -s a y/b
ln -sf a y/b
tree y

tar -czvf out.tgz y
ls

podman pull ubuntu:noble
podman run --rm -ti -v $PWD:/src:ro ubuntu:noble bash

scp out.tgz ubuntu@<ip>:
sha256sum out.tgz
podman inspect ubuntu:noble | grep Digest

ssh ubuntu@<ip>
podman pull ubuntu:noble
podman inspect ubuntu:noble | grep Digest
sha256sum out.tgz

podman run --rm -ti -v $PWD:/src:ro ubuntu:noble bash
```

Session 2:

```
tar -xf /src/out.tgz
ls -al y/
```
