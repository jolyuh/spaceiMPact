import pyglet
import random
import math


def set_img(new_img):
    global img
    img = new_img


def add(mouse_position):
    global a
    a = {
            "sprite":  pyglet.sprite.Sprite(img),
            "immune": False
        }

    a["sprite"].scale = 0.50
    a["sprite"].position = (0, 0)

    def update(dt):
        spr = a["sprite"]
        spr.position = (25, mouse_position[1] - 25)

    a["update"] = update

    return a


def update(dt):
    a["update"](dt)


def draw():
    a["sprite"].draw()

