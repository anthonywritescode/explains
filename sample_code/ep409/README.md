# [what is the `shred` command? (beginner - intermediate)](https://youtu.be/2yt5u5JanwA)

Today I show the `shred` command -- a useful tool for data scrambling when deleting sensitive files!

## Interactive examples

### Bash

```bash
man shred
# echo 'SOME SECRET STUFF' > SECRET.txt
babi SECRET.txt

shred SECRET.txt
less SECRET.txt
rm SECRET.txt
```
