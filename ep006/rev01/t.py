class Location:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'{type(self).__name__}(x={self.x}, y={self.y})'
