# [a file even root can't delete! (chattr) (intermediate)](https://youtu.be/eXUCrIhTsM0)

Today I show how to make a file "immutable" using `chattr` (and describe a few cases I've used this for before!)

## Interactive examples

### Bash

```bash
echo hello hello world > f
sudo chattr +i f

cat f
rm f
sudo rm f

sudo chattr -i f
rm f

nano t.sh
chmod +x !$
./t.sh
./t.sh

chmod 000 t.sh
sudo chattr +i t.sh
./t.sh
cat !$
sudo !!
sudo ./t.sh
```
