import sys


print(f'{sys.stdin.isatty()=}')
print(f'{sys.stdout.isatty()=}')
print(f'{sys.stderr.isatty()=}')


print('foo', file=sys.stdout)
print('bar', file=sys.stderr)


print(f'received input: {input("enter your name: ")}')
