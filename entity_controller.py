from extraobject.extra_object import Pos
from game_config import CONFIG


class EntityController:
    def __init__(self, x, y, speedX, speedY):
        self.pos = Pos(x, y)
        self.speedX = speedX
        self.speedY = speedY

    def move(self):
        pass