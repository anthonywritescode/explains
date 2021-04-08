class SubclassAllMeta(type):
    def __subclasscheck__(self, cls):
        return True


class C(Exception, metaclass=SubclassAllMeta): pass


class D(Exception): pass


breakpoint()

print('is subclass of C?')
print(issubclass(D, C))

try:
    raise D()
except C as e:
    print(f'caught {e}')


OUTPUT = '''\
is subclass of C?
True
Traceback (most recent call last):
  File "t2.py", line 14, in <module>
    raise D()
__main__.D
'''
