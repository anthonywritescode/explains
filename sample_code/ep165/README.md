# [what is virtualenvwrapper + quick start (beginner - intermediate)](https://youtu.be/vnXUBoOqGWQ)

Today I talk about virtualenvwrapper, what it's used for, and how it works under the hood!

## Interactive examples

### Bash

```bash
docker run --rm -ti ubuntu:focal

apt-get update -qq >& /dev/null && DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends python3 python3-distutils python3-pip >& /dev/null
python3 -m pip install virtualenvwrapper
python3 -m pip install babi

export WORKON_HOME=$HOME/.virtualenvs
export PROJECT_HOME=$HOME/workspace
export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3
source /usr/local/bin/virtualenvwrapper.sh

docker ps
docker exec -ti <container_id>

workon foo
mkvirtualenv foo
pip install pyupgrade

mkvirtualenv bar
pip freeze
workon foo
pip freeze

type workon
type mkvirtualenv
```
