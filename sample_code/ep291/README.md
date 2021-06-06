# [atomically replace / delete directories (intermediate - advanced)](https://youtu.be/qEcYqI5NDko)

Today I show how to atomically deal with directories!

## Interactive examples

### Bash

```bash
# delete

mkdir foo
touch foo/bar
mkdir foo/baz
touch foo/baz/wat

tree foo/
rm -rf foo

strace rm -rf foo >& log
less log

mkdir foo && touch foo/bar && mkdir foo/baz && touch foo/baz/wat
tree foo

mkdir trashcan
strace mv foo trashcan/ >& log
less log
ls foo
rm -rf trashcan/ log

# replace

mkdir d1 d2
touch d1/v1
touch d2/v2
ls

mkdir d1 d2 && touch d1/v1 && touch d2/v2
rm -rf d1
mv d2 d1
rm -rf d1

mkdir d1 d2 && touch d1/v1 && touch d2/v2
tree d1 d2

ln -s d1 target
ls -al target
ls -al target/

ln -s d2 newtarget
ls -al

mv -T newtarget target
ls -al

rm target
wget https://github.com/asottile/rename-exchange/releases/download/v2.0.0/rename-exchange_x86_64
chmod +x rename-exchange_x86_64
ls

tree d1 d2
./rename-exchange_x86_64 d1 d2
tree d1 d2
strace ./rename-exchange_x86_64 d1 d2 >& log
less log
```
