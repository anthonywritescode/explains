

things = ['world', 'person', 'a', 'b']

# for i, thing in enumerate(things, start=1):
#     print(f'{i}. hello hello {thing}')

for i in range(1, len(things)):
    print(f'previous: {things[i - 1]}, current: {things[i]}')
