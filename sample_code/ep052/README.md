# [regular expressions crash course (beginner - intermediate)](https://youtu.be/yFRSpPwrJzQ)

Today I give a crash course on the basics of regular expressions and how you might use them to do some basic text matching!

## Interactive examples

### Regexes

- `verbatim text`
  - verbatim text is matched literally
- `.`
  - single character wildcard
- `\`
  - escape character
  - most cases, treat the character after it as a literal character `\.` is `.`
- `^` and `$`
  - anchors
  - `^` matches the beginning of the string
  - `$` matches the end of the string
- `*`, `+`, `?`
  - `*` matches 0 to many of the previous thing
  - `+` matches 1 to many of the previous thing
  - `+` matches 0 or 1 of the previous thing
- `{n}` and `{n,m}`
  - `{n}` is an exact repeat counter, `{2}` matches exactly two of the prevous thing
  - `{,n}` matches 0...n repeats
  - `{n,}` matches n...infinity repeats
  - `{n,m}` matches n...m inclusive repeats
- `[abc]` and `[a-z]`
  - `[abc]` matches a single character that is either `a`, `b` or `c`
  - `[a-f]` matches a single character that is inclusively in the range between `a` and `f`
- `|`
  - exclusive or, match one thing or the other
- `(abc)`
  - grouping mechanism for matching one thing or another

### Bash

```bash
echo hello world

echo hello world | grep -E hello

echo hEllo world | grep -E hello

echo hallo world | grep -E hello

echo hello world | grep -E h.llo

echo hello world. | grep -E world.

echo hello worlds | grep -E world.

echo hello worlds | grep -E 'world\.'

echo hello world. | grep -E 'world\.'

echo hi hello hi | grep -E '^hello'

echo hello hi | grep -E '^hello'

echo hello hi | grep -E 'hello$'

echo hi hello | grep -E 'hello$'

echo hello hi | grep -E '^hello$'

echo hello | grep -E '^hello$'

echo hello | grep 'he*llo'

echo hllo | grep 'he*llo'

echo heeeeeeeeeeeeello | grep 'he*llo'

echo heeeeeeeeeeeeello | grep -E 'he+llo'

echo hllo | grep -E 'he+llo'

echo hllo | grep -E 'he?llo'

echo hello | grep -E 'he?llo'

echo heello | grep -E 'he?llo'

echo heello | grep -E 'he{2}llo'

echo hello | grep -E 'he{2}llo'

echo heeello | grep -E 'he{2}llo'

echo heeello | grep -E 'he{2,}llo'

echo heeello | grep -E 'he{2,}llo'

echo heello | grep -E 'he{2,}llo'

echo heeeeeeeeeeeeeeeeeello | grep -E 'he{2,}llo'

echo heeeeeeeeeeeeeeeeeello | grep -E 'he{,2}llo'

echo hllo | grep -E 'he{,2}llo'

echo hello | grep -E 'he{,2}llo'

echo heello | grep -E 'he{,2}llo'

echo heeello | grep -E 'he{,2}llo'

echo heeello | grep -E 'he{2,5}llo'

echo heeeeeello | grep -E 'he{2,5}llo'

echo hello | grep -E 'h[ea]llo'

echo hullo | grep -E 'h[ea]llo'

echo hullo | grep -E 'h[eau]llo'

echo 'the memory address is 0xdeadbeef' | grep -E '[a-f]+'

echo 'the memory address is 0xdeadbeef' | grep -E '0x[a-f]+'

echo 'the memory address is 0xdeadbeef12341234' | grep -E '0x[a-f]+'

echo 'the memory address is 0xdeadbeef12341234' | grep -E '0x[a-f0-9]+'

echo hello world | grep -E 'h[ea-]llo'

echo hello-world | grep -E 'h[ea-]llo'

echo hello world | grep -E 'hello world|ohai world'

echo ohai world | grep -E 'hello world|ohai world'

echo wat world | grep -E 'hello world|ohai world'

echo wat world | grep -E '(hello|ohai) world'

echo ohai world | grep -E '(hello|ohai) world'

echo hello world | grep -E '(hello|ohai) world'

echo 'hello (world)' | grep -E '(world)'

echo 'hello (world)' | grep -E '\(world\)'
```
