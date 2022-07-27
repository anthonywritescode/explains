import re

with open('src.py') as f:
    contents = f.read()

comment = re.compile('#[^\n]+')

print(comment.sub('', contents))
