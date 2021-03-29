# [sed command basics (beginner - intermediate)](https://youtu.be/fdRL8xME7bQ)

Today I introduce the `sed` command -- I usually use it for basic regex replacement but it's really its own mini language

## Interactive examples

### Bash

```bash
man sed
cat t | sed 's/hello/ohai/g'
sed 's/hello/ohai/g' t
sed 's/hello/ohai/' t

cat t
sed 's|./.|a_a|g' t
sed 's|./.|a_a|g;s/hello/ohai/g' t

echo -e 'aaa\nbbb\ncccc' | sed 's/a+/AAAAA/g'
echo -e 'aaa\nbbb\ncccc' | sed -E 's/a+/AAAAA/g'

sed -i 's/hello/ohai/g' t
cat t

sed '/^ohai/d' t
```
