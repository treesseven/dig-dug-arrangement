WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# import pygame

class Config:
    def __init__(self):
        self.WIDTH = 300
        self.HEIGHT = 364
        self.img_path = "resources/images/"
        self.speed = 1/8
        self.counter = 40
        self.playerX = self.WIDTH - 32 + 16
        self.playerY = 22 + 16

    def load_image(self):
        pass

CONFIG = Config()
