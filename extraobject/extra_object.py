class Pos:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.tuple = [self.x, self.y]

    def update(self, dx, dy):
        self.x += dx
        self.y += dy
        self.tuple = [self.x, self.y]


class Rect:
    def __init__(self, width, height):
        self.width = width
        self.height = height

