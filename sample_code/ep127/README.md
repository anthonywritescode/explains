# [bash: multiple lines to stdin with heredocs (beginner - intermediate)](https://youtu.be/KeO-OGf8Tao)

Today I talk about "heredocs" and how you can pass a more structured "paste" into stdin.

## Interactive examples

### Bash

```bash
babi t
dpkg -S $(which wc)
wc -l t
wc -l < t

echo 'foo' | wc -l
echo $'foo\nbar' | wc -l
wc -l <<< 'foo'

wc -l <<EOF
foo
bar
baz
EOF

# EOF means 'End Of File'

wc -l <<ANTHONY
foo
bar
baz
what
ANTHONY
```
