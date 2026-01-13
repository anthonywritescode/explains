class C:
    @classmethod
    @property
    def classprop(cls):
        print(f'called with {cls}')
        return 5


print(C.classprop)
