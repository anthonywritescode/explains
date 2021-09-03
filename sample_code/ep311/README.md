# [bash: special redirection (intermediate)](https://youtu.be/3f8xjDr789Q)

Today's video is about special redirections in bash to join stdout and stderr when redirecting or piping!

## Interactive examples

### Bash

```bash
bash -c 'echo hi'
bash -c 'echo hi && echo hello 1>&2'
bash -c 'echo hi && echo hello 1>&2' > /dev/null
bash -c 'echo hi && echo hello 1>&2' 2> /dev/null

bash -c 'echo hi && echo hello 1>&2' >& /dev/null
bash -c 'echo hi && echo hello 1>&2' >& f
cat f

bash -c 'echo hi && echo hello 1>&2' 1>&2 > f
bash -c 'echo hi && echo hello 1>&2' 2>&1 > f

# old bash full redirect for both stdout & stderr
bash -c 'echo hi && echo hello 1>&2' &> f
bash -c 'echo hi && echo hello 1>&2' > f 2>&1
cat f

# bash -c 'echo hi && echo hello 1>&2' | grep --color=always ^h
bash -c 'echo hi && echo hello 1>&2' | grep ^h
bash -c 'echo hi && echo hello 1>&2' |& grep ^h
```
