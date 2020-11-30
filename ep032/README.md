# [docker: ADD «url» considered harmful? (intermediate)](https://youtu.be/DazBJeVRA7k)

Today I talk about a feature of `docker` (and dockerfiles) and its limitations and shortcomings and why you probably should `curl` instead.

## Interactive examples

### Bash

```bash
docker build -t test2 .
docker run --rm -ti test2 bash

ls /go
/go/bin/go version
ls -al

docker images | grep test2
docker build -t test3 .
docker images | grep 'test[23]'
```
