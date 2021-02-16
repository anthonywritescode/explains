# [why `docker build --pull`? (intermediate)](https://youtu.be/BP1v7XXlePM)

Today I talk about `docker build --pull` -- what it does and why you probably want it whenever you're building docker images!

## Interactive examples

### Bash

```bash
docker build -t test .
docker run --rm -ti test bash

cat f
exit

docker images
docker build --pull -t test .
docker images
```
