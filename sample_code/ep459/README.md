# [safely stealing github secrets with crypto (intermediate)](https://youtu.be/qjnEZ-3uYjc)

Today I show a hackerman workflow for retrieving lost secrets from github actions by utilizing public-key cryptography!

## Interactive examples

### Bash

```bash
chmod +x enc.sh
./enc.sh asottile 1 hello world

nano t.txt

chmod +x dec.sh
./dec.sh t.txt
```
