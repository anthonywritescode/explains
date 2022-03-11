
lst = list(range(10))
print(f'{lst=}')

for n in reversed(lst):
    if n % 3 == 0:
        lst.remove(n)
    else:
        print(n)

print(f'{lst=}')
