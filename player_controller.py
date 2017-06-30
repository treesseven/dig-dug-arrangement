import pygame
from game_config import CONFIG
from entity_controller import EntityController
from component import *
from extraobject.extra_object import Rect, Pos

length = {
    "walking" : 2
}


class PlayerController(EntityController):
    def __init__(self):
        super().__init__(CONFIG.playerX, CONFIG.playerY, 0, 0)
        self.game_pos = Pos(0, 0)
        self.rotate = "left"
        self.status = "walking"
        self.i = 0
        self.count = 0
        self.image = img_load("player/walking-left-1.png")
        self.images = {}
        self.moving = False
        self.preload()
        self.physic = Physic(Rect(32, 32), self)

    def preload_images(self, status, rotate, length):
        if status not in self.images.keys():
            self.images[status] = {}

        self.images[status][rotate] = []
        for i in range(length):
            self.images[status][rotate].append(img_load("player/{0}-{1}-{2}.png".format(status, rotate, i)))

    def preload(self):
        rots = ["left", "right", "up", "down"]
        for rot in rots:
            self.preload_images("walking", rot, length["walking"])
        add_single_render(self)

    def move(self):
        if self.physic.check_world_bound(self.speedX, self.speedY):
            # x, y = self.get_actual_pos()

            self.pos.update(self.speedX, self.speedY)

    def animation(self):
        if self.moving:
            self.count += 1
            if self.count >= CONFIG.counter:
                self.count = 0
                self.i += 1
                if self.i >= length[self.status]:
                    self.i = 0
            self.image = self.images[self.status][self.rotate][self.i]

    def update(self, keydown):
        rotate = self.rotate
        if not keydown[rotate]:
            self.speedX = 0
            self.speedY = 0
            self.moving = False
        self.move()
        self.animation()
