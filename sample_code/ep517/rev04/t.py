
lst = ['abc', 'Ade', 'foo']
lst.sort(key=lambda s: s.casefold())
print(lst)
