class Location:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    @property
    def loc(self):
        print('computing...')
        return [self.x, self.y]

    @loc.setter
    def loc(self, loc):
        self.x, self.y = loc

    @loc.deleter
    def loc(self):
        self.x = self.y = 0

    def move_to_origin(self):
        self.x = self.y = 0

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
