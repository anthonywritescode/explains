# ["graceful exit" SIGTERM doesn't run finally / destructors ? (intermediate)](https://youtu.be/VVS1xVjhj34)

Today we talk about "graceful exit" and what that means.  we also go over handling SIGTERM -- usually considered a graceful exit and why it doesn't run finalizers -- and then how to make ensure cleanup happens!

## Interactive examples

### Bash

```bash
python t.py

ps -ef | grep python
kill -TERM <process_id>
echo $?
```
