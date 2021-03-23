# [bash: /bin/\[ is an executable ? (intermediate)](https://youtu.be/8kFmJGXa1qk)

Today I talk about if statement "syntax" and why it's not really syntax but a very special builtin emulating the "test" executable!

## Interactive examples

### Bash

```bash
type [

x=1
/bin/[ "$x" -eq 1 ]
echo $?
/bin/[ "$x" -eq 2 ]
echo $?

which \[
/bin/test
/bin/test "$x" -eq 1; echo $?
/bin/test "$x" -eq 2; echo $?

man test
```
