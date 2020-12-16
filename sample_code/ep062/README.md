# [intro to apt (debian / ubuntu) (beginner + intermediate)](https://youtu.be/ctGpRWCi8QU)

Today I talk about both the basics of installing packages on an ubuntu / debian system as well as some more advanced apt / dpkg commands I've picked up over the years.

## Interactive examples

### Bash

Session 1:

```bash
apt --help
apt update
sudo !!
sudo apt install emacs-nox
sudo apt purge emacs-nox
sudo apt autoremove --purge

dpkg -l | wc -l
dpkg -l | less
dpkg -l | grep emacs

aptitude why emacsen-common
dpkg -L emacsen-common
dpkg -L python3-dev

which python3
dpkg -S /usr/bin/python3
dpkg -S /usr/lib/python3
```

Session 2:

```bash
apt-get --help
apt-cache show emacsen-common
```
