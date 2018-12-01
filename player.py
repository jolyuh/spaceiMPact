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

    a["sprite"].scale = 0.2381
    a["sprite"].position = (0, 0)
    global counter
    counter = 0

    def update(dt):
        global counter
        spr = a["sprite"]
        spr.position = (25, mouse_position[1] - 25)
        
        if counter > 2*60 and a["immune"] == True:
            a["immune"] = False
            counter = 0
            
    a["update"] = update

    return a

def update(dt):
    global counter
    counter += 1
    a["update"](dt)


def draw():
    a["sprite"].draw()

