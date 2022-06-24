# [narrow python? len('🙃') == 2??? (intermediate)](https://youtu.be/ht3ezs3O9Yo)

Today I walk through a problem that hopefully no one will ever have again with python: narrow builds.

## Interactive examples

### Python

```python
len('🙃')

len(u'🙃')
len(u'☃')
```

### Bash

```bash
nano default_build.sh
./prefix/bin/python

# cp27-cp27m cp27-cp27mu
```
