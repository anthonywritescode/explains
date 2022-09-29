# [python: don't use urlparse! (beginner - intermediate)](https://youtu.be/ABJvdsIANds)

Today I talk about `urlparse`, archaic url formats, and why you should use something else

## Interactive examples

### Python

```python
import urllib.parse

urllib.parse.urlparse('https://example.com/foo/bar?q=1')
urllib.parse.urlparse('https://example.com/foo/bar?q=1#foo')
urllib.parse.urlparse('https://example.com/foo/bar;foo=1&bar=1?q=1&r=2#foo')
urllib.parse.urlsplit('https://example.com/foo/bar;foo=1&bar=1?q=1&r=2#foo')
urllib.parse.urlunsplit(urllib.parse.urlsplit('https://example.com/foo/bar;foo=1&bar=1?q=1&r=2#foo'))
```

### Bash

```bash
python
```
