class Location:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        self.loc = [self.x, self.y]

    def move_left(self):
        self.x -= 1
        self.update_loc()

    def move_right(self):
        self.x += 1
        self.update_loc()

    def move_up(self):
        self.y -= 1
        self.update_loc()

    def move_down(self):
        self.y += 1
        self.update_loc()

    def update_loc(self):
        self.loc = [self.x, self.y]

    def __repr__(self):
        return f'{type(self).__name__}(x={self.x}, y={self.y})'
