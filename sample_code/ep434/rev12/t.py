import tomllib


with open('t.toml') as f:
    tomllib.load(f)

with open('t.toml', 'rb') as f:
    tomllib.load(f)

with open('t.toml') as f:
    tomllib.loads(f.read())

with open('t.toml', 'rb') as f:
    tomllib.loads(f.read())
