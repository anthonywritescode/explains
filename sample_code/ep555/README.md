# [docker: connecting to localhost outside the container (intermediate)](https://youtu.be/NZGu-9KQVsE)

Today we talk about docker loopback -- how to navigate docker networking to allow connections to the host machine localhost instead of the in-container localhost!

## Interactive examples

### Bash

Session 1:

```bash
docker build -t mycurl .
docker run --rm -ti mycurl bash

curl localhost:8000
exit

curl localhost:8000

docker run --add-host host.docker.internal:host-gateway --rm -ti mycurl bash

cat /etc/hosts
curl host.docker.internal:8000
```

Session 2:

```bash
python3 -m http.server
python3 -m http.server --bind 127.0.0.1

docker network inspect bridge --format='{{(index .IPAM.Config 0).Gateway}}'
python3 -m http.server --bind <Docker IP address>
```

Session 3:

```bash
curl localhost:8000
```
