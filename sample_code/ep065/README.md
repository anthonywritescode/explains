# [special paths: ~, ~user, ., .. (beginner)](https://youtu.be/lyMQASRha9s)

Today I talk about a few special paths and special path shell expansions as well as how you can use them in python!

## Interactive examples

### Python

```python
import os
os.listdir('~')

import os.path
os.path.expanduser('~')
os.listdir(os.path.expanduser('~'))
os.path.expanduser('~root')
```

### Bash

```bash
cd .
mkdir t
cd !$
cd .
rmdir ../t
cd .

chmod +x t.sh
./t.sh

cd ..
tree .
tree

ls ~
echo ~
echo '~'
echo "~"
echo ~root
echo ~<username>
ls ~/<folder_name>
echo ~/<folder_name>
```
