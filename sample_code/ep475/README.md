# [why does python report macos 10.16 ??? (intermediate)](https://youtu.be/Kg8s2YV-aFE)

Today I go over a pretty confusing quirk about python and macos (and how it can break pip in weird ways)

## Interactive examples

### Bash

```bash
python -c 'import platform; print(platform.mac_ver())'
uname -a

SYSTEM_VERSION_COMPAT=1 python -c 'import platform; print(platform.mac_ver())'
SYSTEM_VERSION_COMPAT=0 python -c 'import platform; print(platform.mac_ver())'
```
