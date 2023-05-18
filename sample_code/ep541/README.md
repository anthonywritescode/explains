# [docker: don't mount files! (mount dirs instead) (intermediate)](https://youtu.be/oXfL0UCO9F4)

Today I talk about a little pitfall with mounting in docker -- and why I prefer mounting directories containing files rather than symlinks or files directly!

## Interactive examples

### Bash

Session 1:

```bash
babi t
docker run -v $PWD/t:/t:ro --rm -ti ubuntu:jammy bash

cat t
ls -i t
cat t
exit

mkdir config
docker run -v $PWD/config:/config:ro --rm -ti ubuntu:jammy bash
cat /config/t
cat /config/t
exit

ln -s t current
ls -al

docker run -v $PWD/current:/t:ro --rm -ti ubuntu:jammy bash
ls -i /t
cat /t
```

Session 2:

```bash
babi t.tmp
mv t.tmp t

cat t
ls -i t

echo hi hi >> t

echo hello hello > config/t
cat !$

babi config/t.tmp
mv !$ config/t

touch t2
echo hello hello > t2
ln -sf current t2
cat t2
```
