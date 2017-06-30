from extraobject.extra_object import Pos
from component import *

class Map:
    def __init__(self):

        self.width = 9
        self.height = 10
        # create map
        self.map_tile = []
        self.create_map()
        self.image= img_load("map/0.png")
        self.pos = Pos(self.image.get_width() / 2, self.image.get_height() / 2)
        add_single_render(self)

    def create_map(self):
        self.map_tile.append([True] * self.width)
        for i in range(self.height - 1):
            row = [] * self.width
            self.map_tile.append(row)
