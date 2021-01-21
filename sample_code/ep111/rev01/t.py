import string


class C:
    def __init__(self):
        self.x = 1

    def __getattr__(self, attr):
        if attr in string.ascii_lowercase:
            return self.x
        else:
            raise AttributeError(attr)
