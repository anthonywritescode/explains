import sqlite3
from string.templatelib import Template


def run_query(db, template: Template):
    parts = []
    params = []

    for o in template:
        if isinstance(o, str):
            parts.append(o)
        else:
            parts.append('?')
            params.append(o.value)

    print(''.join(parts))
    return db.execute(''.join(parts), params)


db = sqlite3.connect('db.db')

value = 'v1.5.2'

result = run_query(
    db,
    t'''
        SELECT * FROM repos
        WHERE ref = {value}
    ''',
)

print(list(result))
