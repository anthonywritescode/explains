class MyProperty:
    def __init__(self, func):
        self._func = func

    def __get__(self, inst, owner=None):
        return self._func(inst)


class Location:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    # @property
    @MyProperty
    def loc(self):
        return [self.x, self.y]

    def move_left(self):
        self.x -= 1

    def move_right(self):
        self.x += 1

    def move_up(self):
        self.y -= 1

    def move_down(self):
        self.y += 1

    def __repr__(self):
        return f'{type(self).__name__}(x={self.x}, y={self.y})'
