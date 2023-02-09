# [how to escape this VERY MEAN prank (beginner)](https://youtu.be/ZjSWRGzWo88)

Today I show a very mean prank, but at the same time some knowledge about how to handle special filenames

## Interactive examples

### Bash

```bash
git init wat
cd wat/

touch './-rf $PWD'
git status

rm -rf $PWD
ls

git status
cd ..
ls

git init wat
cd wat/
touch './-rf $PWD'

rm '-rf $PWD'
rm -- '-rf $PWD'
git status

touch './-rf $PWD'
ls .
ls ..
ls ./
rm './-rf $PWD'
touch './-rf $PWD'

echo $'hi\nhello'
touch $'hi\nhello'
ls

git add 'hi
hello'
git ls-files
```
