from typing import LiteralString


def to_jsonb(table: LiteralString, column: LiteralString) -> str:
    return f'''\
        ALTER TABLE {table} ALTER COLUMN {column}
        TYPE jsonb USING {column}::jsonb;
    '''


print(to_jsonb(input('table? '), input('column? ')))
