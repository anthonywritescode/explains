from html import escape
from string.templatelib import Template


def h(t: Template) -> str:
    parts = []
    for o in t:
        if isinstance(o, str):
            parts.append(o)
        else:
            parts.append(escape(o.value))

    return ''.join(parts)


name = 'anthony <script>alert(0)</script> writescode'

print(
    h(
        t'''
            Welcome to my website, <strong>{name}</strong>,
        '''
    )
)
