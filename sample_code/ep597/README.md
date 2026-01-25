# [why did this suddenly OOM?](https://youtu.be/xEfDMjogJnw)

today I show off a bisection I ran on some work code after a particular workflow started mysteriously OOMing!

## Interactive examples

### Bash

```bash
getsentry configoptions sync
gtime -v getsentry configoptions sync

git log --before '2025-02-24'
git checkout <commit_hash>
gtime -v getsentry configoptions sync

git log --before '2025-02-24'
git bisect good <commit_hash>
git log origin/master --before '2025-02-26'
git bisect bad <commit_hash>
git bisect run bash bisect.sh

git diff <commit_hash>^ <commit_hash>
```
