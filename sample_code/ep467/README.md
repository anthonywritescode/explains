# [what is musllinux (PEP 656) (intermediate)](https://www.youtube.com/watch?v=QAbveJB5kk8)

Today I talk about `musllinux` -- what is `musl` and why this matters for wheels!


## Interactive examples

### Bash

```bash
podman run --rm -ti python:3.10.6-alpine sh
which sh
readlink -f $(which sh)

apk add --no-cache gcc
pip3 install libsass
pip3 install cryptography
```
