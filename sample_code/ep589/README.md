# [why don't signals work in docker?](https://youtu.be/0pQxONR73f8)

today we talk about signals in docker, pid 1, and why you always want an init system when running a container!

## Interactive examples

### Bash

Session 1:

```bash
ps -ef | grep -P '\b1\b'

python3 t.py
python3 -u t.py

docker build -t test .

docker run --rm -i -v $PWD:/src:ro test python3 /src/t.py
docker run --rm -i -v $PWD:/src:ro test python3 /src/t.py

docker run --rm -i -v $PWD:/src:ro test bash -c 'python3 /src/t.py'
docker run --rm -i -v $PWD:/src:ro test sh -c 'python3 /src/t.py'

docker run --rm -i -v $PWD:/src:ro test dumb-init sh -c 'python3 /src/t.py'
docker run --rm -i -v $PWD:/src:ro test dumb-init sh -c 'python3 /src/t.py'
docker run --rm -i -v $PWD:/src:ro test dumb-init -v sh -c 'python3 /src/t.py'

kill -l

docker run --init --rm -i -v $PWD:/src:ro test sh -c 'python3 /src/t.py'
```

Session 2:

```bash
docker ps
docker stop <container_id>

docker ps
docker kill --signal INT <container_id>

docker ps
docker kill --signal INT <container_id>
docker kill <container_id>

docker ps -a
docker kill --signal INT <container_id>

docker ps
docker stop <container_id>

docker ps
docker stop <container_id>

docker ps
docker kill --signal INT <container_id>
docker stop <container_id>
```
