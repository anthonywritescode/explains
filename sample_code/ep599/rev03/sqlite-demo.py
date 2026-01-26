import sqlite3
from string.templatelib import Template
from typing import Literal


def convert(value: object, conversion: Literal["a", "r", "s"] | None):
    if conversion == "a":
        return ascii(value)
    elif conversion == "r":
        return repr(value)
    elif conversion == "s":
        return str(value)
    else:
        return value


def run_query(db, template: Template):
    parts = []
    params = []

    for o in template:
        if isinstance(o, str):
            parts.append(o)
        else:
            parts.append('?')
            value = convert(o.value, o.conversion)
            value = format(value, o.format_spec)
            params.append(value)

    print(''.join(parts))
    return db.execute(''.join(parts), params)


db = sqlite3.connect('db.db')

value = 'v1.5.2'

result = run_query(
    db,
    f'''
        SELECT * FROM repos
        WHERE ref = {value!r}
    ''',
)

print(list(result))
