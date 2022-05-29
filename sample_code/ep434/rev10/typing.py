from typing import LiteralString


def execute_query(s: LiteralString) -> ...:
    ...


execute_query('SELECT * FROM USERS')

users = '...'
execute_query('SELECT * FROM {}'.format(users))
