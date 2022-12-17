# [why I use the colon (:) command (intermediate)](https://youtu.be/onkNf1AKSgg)

Today we talk about a fairly useless command and why I like to use it in shell scripts!

## Interactive examples

### Bash

```bash
: foo bar

bash t.sh
chmod +x t.sh
./t.sh

true
false

true; echo $?
false; echo $?

true hello hello
false hello hello
echo $?

:; echo $?

type :
type true
type false
type \true

\true
/bin/true
```
