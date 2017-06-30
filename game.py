import pygame
from game_config import CONFIG
from player_controller import PlayerController
from map import Map
from component import *
direction = ["left", "right", "up", "down"]


class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((CONFIG.WIDTH, CONFIG.HEIGHT))
        self.key_down = {}
        self.renderer = []
        self.preload()
        set_world_bound(left = 0, right = 300, top = 22, bottom= 364)

    def preload(self):
        for key in direction:
            self.key_down[key] = False

        img_path = CONFIG.img_path
        self.map = Map()
        self.player = PlayerController()

    def handle_rotate(self, rotate):
        rot = {
            "left"  : [-CONFIG.speed, 0],
            "right" : [CONFIG.speed, 0],
            "up"    : [0, -CONFIG.speed],
            "down"  : [0, CONFIG.speed]
        }

        self.player.rotate = rotate
        self.player.speedX = rot[rotate][0]
        self.player.speedY = rot[rotate][1]
        self.key_down[rotate] = True
        self.player.moving = True

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.handle_rotate("left")
            if event.key == pygame.K_RIGHT:
                self.handle_rotate("right")
            if event.key == pygame.K_UP:
                self.handle_rotate("up")
            if event.key == pygame.K_DOWN:
                self.handle_rotate("down")

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                self.key_down["left"] = False
            if event.key == pygame.K_RIGHT:
                self.key_down["right"] = False
            if event.key == pygame.K_UP:
                self.key_down["up"] = False
            if event.key == pygame.K_DOWN:
                self.key_down["down"] = False


    def update(self):
        self.player.update(self.key_down)
