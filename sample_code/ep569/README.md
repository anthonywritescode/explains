# [using git bisect to find a bug in nodejs (intermediate)](https://youtu.be/cSd5GGrj2VA)

today I walk through how I figured out a zip corruption problem and when it was introduced in nodejs!

## Setup commands

```bash
podman run --rm -ti node:20.11.1 bash
# OR
docker run --rm -ti node:20.11.1 bash

apt update
apt install nano zip
npm install unzipper
```

## Interactive examples

### Bash

Session 1:

```bash
mkdir zips qq && cd qq
wget -q -O inner.zip https://github.com/getsentry/sentry-android-gradle-plugin/releases/download/4.3.0/sentry-android-gradle-plugin-4.3.0.zip

file inner.zip
zipinfo inner.zip
zipdetails inner.zip

zip outer.zip inner.zip
unzip -l outer.zip

nano t.mjs
node t.mjs outer.zip out-1
ls out-1/

node t.mjs out-1/inner.zip out-2
node --version

nano t.sh
chmod +x t.sh
bash t.sh
```

Session 2:

```bash
git clone git@github.com:nodejs/node
git remote -v

git bisect start
git bisect bad v18.19.0
git bisect good v17.0.0

echo $CC

chmod +x ../repro/{bisect,repro}.sh
git bisect run ../repro/bisect.sh
```
