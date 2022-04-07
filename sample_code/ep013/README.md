# [shell bling strings! (beginner - intermediate)](https://youtu.be/fhhznv4E1pI)

Quick video talking about a little shell feature that I wish I had know about earlier :)

## Interactive examples

### Bash

```bash
echo -e 'foo\tbar'

echo 'foo\tbar'

/bin/echo -e 'foo\tbar'

echo $'echo\tbar'

python -c 'import sys;print(sys.argv)' -- $'foo\tbar'

python -c 'import sys;print("\n".join(sys.argv))' -- $'foo\tbar'

python -c 'import sys;print("\n".join(sys.argv))' -- 'foo\tbar'

python -c 'import sys;print("\n".join(sys.argv))' -- "$(echo -e 'foo\tbar')"

x=foo

echo '$x bar'

echo "$x bar"

echo 'asdf<Ctrl-v-TAB>bar'

echo 'asdf<Ctrl-v-ESC>asdf'
```
