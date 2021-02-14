# [repeatedly checking command output (beginner - intermediate)](https://youtu.be/DUxS7zOhu1U)

Today I show you a command I wish I had known about earlier: watch!  also featuring younger programming me when I didn't know about this command!

## Interactive examples

### Bash

Session 1:

```bash
watch ls -al
watch -n.1 "ls -al | tac"
watch -d "ls -al | tac"
watch -d "ls -al"
```

Session 2:

```bash
touch foo
rm foo
```
