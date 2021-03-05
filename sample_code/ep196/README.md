# [intro to git lfs (intermediate)](https://youtu.be/c6BRKcO5WxE)

Today I talk about git-lfs -- a way to store bulky files outside of the repository so they don't make your clones super slow and sad

## Interactive examples

### Bash

```bash
git clone https://github.com/Apress/repo-with-large-file-storage
cd repo-with-large-file-storage
du -hs .
ls
nano LargeFile.zip

apt install git-lfs
git lfs install
nano .git/hooks/post-checkout
nano .git/hooks/pre-push
nano .gitattributes

apt install file
file LargeFile.zip
git lfs fetch
# git lfs checkout

cd ..
git clone https://github.com/Apress/repo-with-large-file-storage repo2
cd repo2
ls
du -hs LargeFile.zip
```
