# -----------------------IMAGE---------------------------------------#
import pygame

renderer = []


def img_load(path):
    img_path = "resources/images/" + path
    return pygame.image.load(img_path)


def add_single_render(object):
    global renderer
    renderer.append(object)


def render(screen):
    for object in renderer:
        screen.blit(object.image, (object.pos.x - object.image.get_width()/2,
                                   object.pos.y - object.image.get_height()/2))

#-----------------------------WORLD_BOUND-----------------------
world_bound = {}

def check_world_bound(object):
    pass


def set_world_bound(left, top, right, bottom):
    global world_bound
    world_bound["left"] = left
    world_bound["top"] = top
    world_bound["bottom"] = bottom
    world_bound["right"] = right


# ----------------------------PHYSIC----------------------------

physics_group = []


def move(object):
    object.pos.update(object.speedX, object.speedY)


def add_physics(object):
    physics_group.append(object)


def do_physics():
    for object in physics_group:
        move(object)


class Physic:
    def __init__(self, rectangle, object):
        self.width = rectangle.width
        self.height = rectangle.height
        self.pos = object.pos

    def check_world_bound(self, speedX, speedY):
        left = self.pos.x - self.width / 2 + speedX
        right = self.pos.x + self.width / 2 + speedX
        top = self.pos.y - self.height / 2 + speedY
        bottom = self.pos.y + self.height / 2 + speedY
        print(bottom, left, right, top)
        if left >= world_bound["left"] and right <= world_bound["right"] and \
            top >= world_bound["top"] and bottom <= world_bound["bottom"]:
            return True
        return False

# ------------------------------ANIMATION---------------------------------------################################

