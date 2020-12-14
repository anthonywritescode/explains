# [what is deadsnakes? (beginner - intermediate)](https://youtu.be/Xe40amojaXE)

Today I go over what the deadsnakes PPA is and how I started maintaining backport and forwardport python versions!

## Interactive examples

### Bash

```bash
docker run --rm -it ubuntu:bionic bash

# container shell
apt-get update -qqq && apt-get install -yqqq gnupg2 software-properties-common >& /dev/null
add-apt-repository ppa:deadsnakes

apt-get install python3.9-dev
python3.9

add-apt-repository ppa:deadsnakes/nightly
```
