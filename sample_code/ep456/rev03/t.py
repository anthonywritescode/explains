from __future__ import annotations
from typing import Match

import re

with open('src.py') as f:
    contents = f.read()

comment = re.compile('#([^\n]+)')


def cb(match: Match[str]) -> str:
    return f'#{len(match[1]) * "."}'


print(comment.sub(cb, contents), end='')
