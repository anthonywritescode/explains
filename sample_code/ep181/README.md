# [argparse: making a command wrapper (parse\_known\_args) (intermediate)](https://youtu.be/sCbC8hkg_xs)

Today I show how to use argparse and parse_known_args to create a wrapper commandline tool!

## Interactive examples

### Bash

```bash
python docker_hostenv.py --rm -ti ubuntu:focal bash
env
exit

python docker_hostenv.py --no-hostenv --rm -ti ubuntu:focal bash
env | grep HOST
exit

python docker_hostenv.py --help --no-hostenv --rm -ti ubuntu:focal bash
python -m pydoc argparse.ArgumentParser
```
