# [don't put passwords in commands! (beginner - intermediate)](https://youtu.be/SqXOchNKV_c)

Today I talk about why it's a bad idea to call commands with passwords in them and a few strategies you can use to design programs to avoid that (as well as a cool tip to keep commands out of the history file!)

## Interactive examples

### Notes

```text
Storing passwords/secrets:

- configuration file
- software for storing certificates, credentials, keys, passwords and any secrets in general:
    - OS specific solution:
        - Keyring / Seahorse (Linux)
        - Keychain (MacOS)
        - Credential Manager (Windows)
        - Password Managers (generic software)
    - Vault (self-hosted services)
    - Cloud specific/hosted services
- environment variable
- standard input
```

### Bash

Session 1:

```bash
python -c 'import time; time.sleep(10)'
python -c 'import time; time.sleep(10)' -p 'bad password'
python -c 'import time; time.sleep(1000)' -p 'bad password'
history | tail -10
  echo secret
history | tail -10
```

Session 2:

```bash
ps -ef | grep sleep
ps -wwwef | grep sleep
sudo -u nobody ps -wwwef | grep sleep
# sudo -u nobody -- ps -wwwef | grep sleep
```
