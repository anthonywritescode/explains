# [docker takes so much disk! (beginner - intermediate)](https://youtu.be/TSjZrubRfXo)

Today I go over a command which helps cull some of the extraneous disk usage that docker causes!

## Interactive examples

### Bash

```bash
docker images
docker run ubuntu:focal echo hi
docker ps -a

docker system prune
docker system prune -f
```
