# [docker: deleting files makes your image bigger! (intermediate)](https://youtu.be/4kBfXrE0xpo)

Today I dive into the image format for docker images and explain why deleting files actually makes your image bigger!

## Interactive examples

### Bash

```bash
docker build -t test .
podman --version
docker --version
docker history test
docker images

podman image save test > test.tgz
file test.tgz
du -hs test.tgz
ls
mkdir out
cd !$
ls
tar -xf ../test.tgz
ls
cat repositories
cat repositories && echo
jq . manifest.json
jq . <config_hash_from_manifest_file>.json

mkdir layer0
cd !$
ls
tar -xf ../<layer0_hash>.tar
ls run
tree
ls -al run
cat run/.containerenv
ls -al

cd ..
mkdir layer1
ls
tar -xf ../<layer1_hash>.tar
ls -al

cd ..
mkdir layer2
cd layer2
tar -xf ../<layer2_hash>.tar
ls
ls usr/
ls usr/bin/
```
