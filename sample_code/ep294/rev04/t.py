class C:
    @staticmethod
    def f():
        print('f was called')

    # @classmethod
    def g(cls):
        print(f'g was called from {cls=}')
