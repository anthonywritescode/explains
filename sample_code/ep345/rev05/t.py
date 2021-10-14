import itertools


things = ['world', 'person', 'a', 'b']

# for i in range(1, len(things)):
#     print(f'previous: {things[i - 1]}, current: {things[i]}')

for thing1, thing2 in zip(things, itertools.islice(things, 1, len(things))):
    print(f'previous: {thing1}, current: {thing2}')
