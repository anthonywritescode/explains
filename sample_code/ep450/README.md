# [regex backreferences (intermediate)](https://youtu.be/gPMpRw1xUA8)

Today I talk about back references in regular expressions and the 3 contexts they can appear in (in the pattern, after matching, and while replacing)

## Interactive examples

### Notes

```text
0th group is the whole string

inside a pattern:
    - \1: positional groups
    - (?P=name): named groups

inside the match:
    - match[1]: positional groups
    - match['name']: named groups

in replacements:
    - \1: positional groups
    - \g<1>: positional groups
    - \g<name>: named groups
```

### Python

```python
import re

'foo'
"foo"

pat = re.compile('[\'"].*[\'"]')
pat.match('"foo"')
pat.match("'foo'")
pat.match("'foo\"")

pat = re.compile(r'([\'"]).*\1')
pat.match("'foo\"")
pat.match("'foo'")
pat.match('"foo"')

pat = re.compile(r'(?P<quote>[\'"]).*\1')
pat.match('"foo"')

pat = re.compile(r'(?P<quote>[\'"]).*(?P=quote)')
pat.match('"foo"')

match = pat.match('"foo"')
match[1]
match['quote']

match.group('quote')
match.group(0)
match.group(1)

pat = re.compile(r'(?P<quote>[\'"])(?P<meat>.*)(?P=quote)')
pat.match('"foo"')
match = pat.match('"foo"')
match['meat']
match['quote']

pat.sub(r'\1hello \2\1', '"foo"')
pat.sub(r'\g<quote>hello \g<meat>\g<quote>', '"foo"')
pat.sub(r'\g<1>hello \g<2>\g<1>', '"foo"')

pat.sub(r'\1123deadbeaf \2\1', '"foo"')
pat.sub(r'\g<1>123deadbeaf \2\1', '"foo"')
```

### Bash

```bash
python
```
