# [faster git recloning\* (intermediate)](https://youtu.be/rLHNAiLv7r0)

*with a catch -- and a convenient fix!

## Setup commands

```bash
git clone git@github.com:deadsnakes/python3.13-nightly /tmp/python3.13-nightly
```

## Interactive examples

### Bash

```bash
git clone --reference /tmp/python3.13-nightly git@github.com:deadsnakes/python3.13-nightly
cd python3.13-nightly/
git status

mv /tmp/python3.13-nightly{,old}
git status

cat .git/objects/info/alternates
git clone --dissociate --reference /tmp/python3.13-nightlyold git@github.com:deadsnakes/python3.13-nightly
cd python3.13-nightly/
git status

mv /tmp/python3.13-nightlyold{,old}
git status
ls .git/objects/info/
```
