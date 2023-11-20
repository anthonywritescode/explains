# [new 3.12 f-strings syntax! (intermediate)](https://youtu.be/BkexKFfrAeo)

Today I show off (again) the new f-strings syntax in 3.12 and the problems it solves from previous versions

## Interactive examples

### Python

```python
things = ['hello', 'hello', 'world']
''.join(things)

print(f'problems:\n\n{"\n".join(things)}')
print(f'problems:\n\n{"n".join(things)}')

print(f'hello {'thing'}')

print(f'problems:\n\n{"\n".join(things)}')
print(f'problems:\n\n{'\n'.join(things)}')

f'{f'{f'{f'{'hello'}'}'}'}'

f'{
# hello
'world'
}'

f'{
 ''()
}'

f'{''()}'
```

### Bash

```bash
python3.11
python3.12
```
