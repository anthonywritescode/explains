# [10 protips I wish I knew sooner as a software dev (beginner)](https://youtu.be/_wcVyhfyaeE)

Here's ten quick things you can learn to level up your bash / terminal skills.

## Interactive examples

### Bash

Session 1:

```bash
# Ctrl-r
git clone git@github.com:asottile/babi

echo mistake
fc
# Ctrl-x-e

ls /proc/1/exe
sudo !!
apt update
sudo !!

cd babi/
sed -i 's/babi/nano/g' README.md
git commit -am "!!"

cd ..
babi t.py
# echo "print('hello hello world')" > t.py
python !$

rm -rf babi/
git clone git@github.com:asottile/babi babi
cd !$
cd ..

mkdir y
cd !$

echo # Alt-.

echo 'a<Ctrl-v-TAB>b'

python t.py
# Ctrl-\

# Github keyboard shortcut for permalink: y
# Github keyboard shortcut cheatsheet: Shift-/ or Shift-?

podman ps
podman exec -ti <container_hash_id> bash
ls
ls /root/.ssh/authorized_keys
exit

ssh -p 41807 root@0.0.0.0
ps

# Enter-~-?
while true; do true; done
# Enter-~-.

podman exec -ti <container_hash_id> bash
ps -ef
exit

# Ctrl-Shift-u
echo ☃
echo 🙃
echo —
```

Session 2:

```bash
/usr/sbin/sshd -D -p 9001
```
