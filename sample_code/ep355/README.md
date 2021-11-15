# [why remove the python GIL? (intermediate - advanced)](https://youtu.be/6g79qGQo2-Q)

Today we talk about the "global interpreter lock" in python and why it currently limits multithreading to 100% usage (and what could be done if it were lifted)

## Interactive examples

### Bash

```bash
python t.py
python t2.py

ps -ef | grep python
pstree -halp <process_id>
```
