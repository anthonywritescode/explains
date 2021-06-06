# [☃.com and punycode / idna (beginner - intermediate)](https://youtu.be/MMkOWqJkxeo)

Today we talk about a fun little domain name ☃.com (or canonically xn--n3h.com) and how that works!

## Interactive examples

### Python

```python
'☃'.encode('punycode')
'www.☃.com'.encode('punycode')
'www.☃.com'.encode('idna')

import codecs

codecs.encode('www.☃.com', 'idna')

'🙃'
'www.🙃.com'.encode('idna')
```

### Bash

```bash
echo ☃
```
