# [bash: passing string as stdin (beginner - intermediate)](https://youtu.be/Xf_82stIbB8)

Here's a little tip that I hope will make your bash scripts easier to write!  this helps avoid unnecessary cat / echo calls

## Interactive examples

### Bash

```bash
x="foo bar baz"
echo "$x"
echo "$x" | python -c 'import sys; print(sys.stdin.buffer.read())'
python -c 'import sys; print(sys.stdin.buffer.read())' <<< "$x"
python -c 'import sys; print(sys.stdin.buffer.read())' <<< asdfasdfasdf
```
