import pyglet
import math


def set_img(new_img):
    global img
    img = new_img


def add(mouse_position):
    global pl
    pl = {
            "sprite":  pyglet.sprite.Sprite(img),
            "immune": False
        }

    pl["sprite"].scale = 0.2381
    pl["sprite"].position = (0, 0)
    global counter
    counter = 0

    def update_player(dt):
        global counter
        spr = pl["sprite"]

        target = (25 + 200 * ((mouse_position[0] - 100)/720), mouse_position[1] - 25)
        spr.position = (spr.position[0] + (target[0]-spr.position[0])/4, spr.position[1] + (target[1]-spr.position[1])/4)
        
        if counter > 2*60 and pl["immune"] is True:
            pl["immune"] = False
            counter = 0

        if pl["immune"]:
            pl["sprite"].color = (100+math.floor(77+77*math.sin(counter)), 100, 100)
        else:
            pl["sprite"].color = (255, 255, 255)
            
    pl["update"] = update_player

    return pl


def update(dt):
    global counter
    counter += 1
    pl["update"](dt)


def draw():
    pl["sprite"].draw()
