
class mcs(type):
    def __subclasscheck__(self, tp):
        return True


class Weird(Exception, metaclass=mcs):
    pass
