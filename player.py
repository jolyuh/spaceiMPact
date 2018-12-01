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

        target = ( 25 + 200 * ((mouse_position[0] - 100 )/720) , mouse_position[1] - 25)
        spr.position = ( spr.position[0] + (target[0]-spr.position[0])/4 , spr.position[1] + (target[1]-spr.position[1])/4 )
        
        if counter > 2*60 and a["immune"] is True:
            a["immune"] = False
            counter = 0

        if a["immune"]:
            a["sprite"].color = (100+math.floor(77+77*math.sin(counter) ),100,100)
        else:
            a["sprite"].color = (255,255,255)
            
    a["update"] = update

    return a


def update(dt):
    global counter
    counter += 1
    a["update"](dt)


def draw():
    a["sprite"].draw()
