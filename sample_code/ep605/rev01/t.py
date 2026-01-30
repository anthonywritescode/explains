def to_jsonb(table: str, column: str) -> str:
    return f'''\
        ALTER TABLE {table} ALTER COLUMN {column}
        TYPE jsonb USING {column}::jsonb;
    '''


print(to_jsonb(input('table? '), input('column? ')))
