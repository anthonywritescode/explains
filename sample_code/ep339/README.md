# [debugging a failed docker build (intermediate)](https://youtu.be/hd1AKYGiWNk)

Today we talk about two techniques for debugging a failed docker build!

## Interactive examples

### Bash

```bash
docker build -t test .
docker ps
docker ps -a

docker commit <container_id> someimg
docker run --rm -ti someimg bash

ls
cat log
exit

docker rmi someimg
docker run --rm -ti <intermediate_container_id> bash

sh -c 'echo some error > log; exit 1'
echo $?
cat log

# bonus commands
podman build -t test .
podman ps
podman ps -a
podman ps -a --external

podman build -t test . --force-rm=false
podman ps -a --external
```
