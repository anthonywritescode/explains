# [docker run: always use --rm! (beginner - intermediate)](https://youtu.be/0vxIyXgkihA)

Today I talk about a gotcha with `docker run` and why you should always use `--rm` -- I also show how to clean up if you've been running docker without this flag!

## Interactive examples

### Bash

Session 1:

```bash
docker run -ti ubuntu:focal bash
docker ps
docker ps -a

docker run -ti --rm ubuntu:focal bash
docker ps -a
docker system prune
```

Session 2:

```bash
echo hi
exit
```
